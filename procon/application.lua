-- PROCON // PK-AA33
-- 
-- ESP32 & NodeMCU based replacement for the PK-AA32 PROCON in the
-- No. 5 Crossbar Maintenance Data Terminal.  This allows the 5XB to
-- report errors to a computer at the Switching Control Center instead
-- of the card punch associated with the switch.
-- 
-- Astrid Smith, 2019
-- Connections Museum

require "sjson"
require "gpio"
require "bit"

server = "http://192.168.0.204:5220/punch"

-- check all this nonsense, clearly

dist = {["OPEN"] = 1, ["CLOSED"] = 0}

-- scan point shows HIGH=0 on ground, LOW=1 on battery or open
scan = {[0] = 1, [1] = 0, ["OPEN"] = 0, ["GND"] = 1}

-- logic is inverted from what gpio calls it ...
logic = {[0] = 1, [1] = 0, ["LOW"] = 1, ["HIGH"] = 0, [false] = 1, [true] = 0}

-- yes the matrixes are somewhat fuckily arranged. see SD-28111-01 sh B2, FS 3
distpts_order =
   {"S4", "S3", "S2", "S1", "S0", "RSV0.5",
    "RSV1.0", "S8", "S7", "S6", "S5", "TRC",
    "MB", "CMJ", "CMN", "ARLK", "STRA", "STR",
    "RSV3.0", "RSV3.1", "RSV3.2", "RSV3.3", "RSV3.4", "RSV3.5"
   }

distpts_cache =
   {
      { "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN" },
      { "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN" },
      { "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN" },
      { "OPEN", "OPEN", "OPEN", "OPEN", "OPEN", "OPEN" }
   }

scanpts_order =
   {"07", "06", "05", "04", "03", "02", "01", "00", "STRA1", "STR",
    "15", "14", "13", "12", "11", "10", "09", "08", "TRC", "SPL",
    "23", "22", "21", "20", "19", "18", "17", "16", "ROS", "MB",
    "BWX1", "BWX0", "29", "28", "27", "26", "25", "24", "RSV3.8", "RSV3.9",
    "37", "36", "35", "34", "33", "32", "31", "30", "RSV4.8", "RSV4.9",
    "45", "44", "43", "42", "41", "40", "39", "38", "RSV5.8", "RSV5.9",
    "53", "52", "51", "50", "49", "48", "47", "46", "RSV6.8", "RSV6.9",
    "61", "60", "59", "58", "57", "56", "55", "54", "RSV7.8", "RSV7.9",
    "69", "68", "67", "66", "65", "64", "63", "62", "RSV8.8", "RSV8.9",
    "77", "76", "75", "74", "73", "72", "71", "70", "RSV9.8", "RSV9.9",
    "85", "84", "83", "82", "81", "80", "79", "78", "RSV10.8", "RSV10.9",
    "91", "90", "BWX3", "BWX2", "89", "88", "87", "86", "RSV11.8", "RSV11.9",
    "99", "98", "97", "96", "95", "94", "93", "92", "RSV12.8", "RSV12.9",
    "107", "106", "105", "104", "103", "102", "101", "100", "RSV13.8", "RSV13.9",
    "115", "114", "113", "112", "111", "110", "109", "108", "RSV14.8", "RSV14.9",
    "RSV15.0", "RSV15.1", "RSV15.2", "RSV15.3", "119", "118", "117", "116", "RSV15.8", "RSV15.9"
   }

distpts = {}
scanpts = {}
for k, v in pairs(distpts_order) do
   distpts[v] = { ["bit"] = (k-1) % 6, ["row"] = math.floor((k-1) / 6) }
end
for k, v in pairs(scanpts_order) do
   scanpts[v] = { ["bit"] = (k-1) % 10, ["row"] = math.floor((k-1) / 10) }
end

function get_scanpt(name)
   pin = scanpts[name]
   return pin.row, pin.bit
end
function get_distpt(name)
   pin = distpts[name]
   return pin.row, pin.bit
end

leads = {}
-- and now to enumerate the GPIO leads ...
leads["A1"] = 13
leads["A2"] = 12
leads["A3"] = 14
leads["A4"] = 18
leads["C1"] = 19
leads["MSYN"] = 21
leads["SSYN"] = 22
leads["D00"] = 23
leads["D01"] = 25
leads["D02"] = 26
leads["D03"] = 27
leads["D04"] = 32
leads["D05"] = 33
leads["D06"] = 34
leads["D07"] = 35
leads["D08"] = 4
leads["D09"] = 5


function setup_leads()
   gpio.config({gpio = leads.A1,   dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.A2,   dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.A3,   dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.A4,   dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})

   gpio.config({gpio = leads.C1, dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.MSYN, dir = gpio.OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.SSYN, dir = gpio.IN})

   gpio.config({gpio = leads.D00,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D01,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D02,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D03,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D04,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D05,  dir = gpio.IN_OUT, opendrain = 1, pull = gpio.FLOATING})
   gpio.config({gpio = leads.D06,  dir = gpio.IN})
   gpio.config({gpio = leads.D07,  dir = gpio.IN})
   gpio.config({gpio = leads.D08,  dir = gpio.IN})
   gpio.config({gpio = leads.D09,  dir = gpio.IN})
end

function restore_leads()
   gpio.write(leads.MSYN, 1)
   gpio.write(leads.C1, 1)

   gpio.write(leads.A1, 1)
   gpio.write(leads.A2, 1)
   gpio.write(leads.A3, 1)
   gpio.write(leads.A4, 1)

   gpio.write(leads.D00, 1)
   gpio.write(leads.D01, 1)
   gpio.write(leads.D02, 1)
   gpio.write(leads.D03, 1)
   gpio.write(leads.D04, 1)
   gpio.write(leads.D05, 1)
end

-- read a word from the scan points (10 bits)
function read_row(rownr)
   -- gpio.HIGH==1 but the bus is active-low logic, ugh, see the
   -- `logic" table

   -- set C1 lead to "read" = 0
   gpio.write(leads.C1, logic[0])

   -- write address to the A1,A2,A3,A4 leads
   --
   -- nice.  instead of updating the lua (which is from 2008) they
   -- decided to implement bitwise operations in an addon module.
   gpio.write(leads.A1, logic[bit.isset(rownr, 0)])
   gpio.write(leads.A2, logic[bit.isset(rownr, 1)])
   gpio.write(leads.A3, logic[bit.isset(rownr, 2)])
   gpio.write(leads.A4, logic[bit.isset(rownr, 3)])

   -- strobe MSYN lead
   gpio.write(leads.MSYN, logic[1])

   -- observe for SSYN
   j = 0
   while (gpio.read(leads.SSYN) == 1) do
      j = j+1
   end

   -- read from D00 thru D09
   d0 = gpio.read(leads.D00)
   d1 = gpio.read(leads.D01)
   d2 = gpio.read(leads.D02)
   d3 = gpio.read(leads.D03)
   d4 = gpio.read(leads.D04)
   d5 = gpio.read(leads.D05)
   d6 = gpio.read(leads.D06)
   d7 = gpio.read(leads.D07)
   d8 = gpio.read(leads.D08)
   d9 = gpio.read(leads.D09)

   -- drop MSYN
   gpio.write(leads.MSYN, logic[0])
   restore_leads()

   -- return that data in some format
   return { scan[d0], scan[d1], scan[d2], scan[d3], scan[d4], scan[d5], scan[d6], scan[d7], scan[d8], scan[d9] }
end

-- write a word to the dist points (6 bits)
function write_row(rownr, values)
   -- write address to the A1,A2 leads
   gpio.write(leads.A1, logic[bit.isset(rownr, 0)])
   gpio.write(leads.A2, logic[bit.isset(rownr, 1)])

   -- write data to leads D00 thru D05
   gpio.write(leads.D00, dist[values[1]])
   gpio.write(leads.D01, dist[values[2]])
   gpio.write(leads.D02, dist[values[3]])
   gpio.write(leads.D03, dist[values[4]])
   gpio.write(leads.D04, dist[values[5]])
   gpio.write(leads.D05, dist[values[6]])
   
   -- set C1 lead to "write" = 1
   gpio.write(leads.C1, logic[1])

   -- strobe MSYN lead
   gpio.write(leads.MSYN, logic[1])

   -- observe for SSYN
   j = 0
   while (gpio.read(leads.SSYN) == logic[0]) do
      j = j+1
   end

   -- drop MSYN
   gpio.write(leads.MSYN, logic[0])
   restore_leads()

   return
end

function write_named_distpt(name, value)
   rownr, bitnr = get_distpt(name)
   -- because lists here start at 1
   distpts_cache[rownr+1][bitnr+1] = value
   write_row(rownr, distpts_cache[rownr+1])
end

function read_named_scanpt(name)
   rownr, bitnr = get_scanpt(name)
   rowdat = read_row(rownr)
   return rowdat[bitnr]
end

-- read all the scan points
function read_all()
   r = {}
   r[0] = read_row(0)
   r[1] = read_row(1)
   r[2] = read_row(2)
   r[3] = read_row(3)
   r[4] = read_row(4)
   r[5] = read_row(5)
   r[6] = read_row(6)
   r[7] = read_row(7)
   r[8] = read_row(8)
   r[9] = read_row(9)
   r[10] = read_row(10)
   r[11] = read_row(11)
   r[12] = read_row(12)
   r[13] = read_row(13)
   r[14] = read_row(14)
   r[15] = read_row(15)
   return r
end

function close_scan_relay(name)
   write_named_distpt(name, "CLOSED")
end

-- read one row of a card from the trouble record
function read_relay_row(name)
   -- read all rows
   trouble[name] = read_all()
   write_named_distpt(name, "OPEN")
   return
end

function take_trouble_record(indication)
   -- indication is "STR" or "STRA"
   read_full_card()
   write_named_distpt("TRC", "CLOSED")
   -- wait for scanpt STR or STRA to clear
   while (read_named_scanpt(indication) == 1) do
   end
   write_named_distpt("TRC", "OPEN")
end

function state_idle()
   -- print("looking for trouble?")
   
   if (ONLINE == 1) then
      write_named_distpt("MB", "OPEN")
   else
      write_named_distpt("MB", "CLOSED")
   end

   if (read_named_scanpt("STRA1") == 1) then
      print("starting special trouble")
      trouble_type = "express"
      return {["next"]= "s8"}
   elseif (read_named_scanpt("STR") == 1) then
      print("starting normal trouble")
      trouble_type = "normal"
      return {["next"]= "s8"}
   else
      return {["next"]= "idle"}
   end
end

function state_transmit()
   print(trouble_type)
   local tbl = sjson.encode(trouble)
   http.post(server, "Content-Type: application/json\r\n", tbl,
             function(status_code, body, headers)
                cur_state = "release"
             end )
   trouble = {}
   trouble_type = nil

   return {["next"]= "transmit_wait"}
end

function state_transmit_wait()
   return {["next"]= "transmit_wait"}
end

function state_release()
   write_named_distpt("TRC", "CLOSED")
   if (trouble_type == "express") then
      indication = "STRA1"
   else
      indication = "STR"
   end

   while (read_named_scanpt(indication) == 1) do
   end
   write_named_distpt("TRC", "OPEN")
   
   return {["next"]= "idle"}
end

function state_init()
   write_named_distpt("MB", "CLOSED")
   mb_scan = 0
   mb_scan = read_named_scanpt("MB")
   print("MB x, scanpoint is "..mb_scan)

   write_named_distpt("MB", "OPEN")
   mb_scan = read_named_scanpt("MB")
   print("MB -, scanpoint is "..mb_scan)
   while (mb_scan ~= 0) do
      mb_scan = read_named_scanpt("MB")
      print("MB x, scanpoint is "..mb_scan)
   end

   return {["next"]= "idle"}
end

ms = 1
sec = 1000

state = {
   ["start"]= state_init,
   ["idle"]= state_idle,
   ["s8"]= function() close_scan_relay("S8"); return {["next"]= "r8", ["delay"]= 32*ms} end,
   ["s7"]= function() close_scan_relay("S7"); return {["next"]= "r7", ["delay"]= 32*ms} end,
   ["s6"]= function() close_scan_relay("S6"); return {["next"]= "r6", ["delay"]= 32*ms} end,
   ["s5"]= function() close_scan_relay("S5"); return {["next"]= "r5", ["delay"]= 32*ms} end,
   ["s4"]= function() close_scan_relay("S4"); return {["next"]= "r4", ["delay"]= 32*ms} end,
   ["s3"]= function() close_scan_relay("S3"); return {["next"]= "r3", ["delay"]= 32*ms} end,
   ["s2"]= function() close_scan_relay("S2"); return {["next"]= "r2", ["delay"]= 32*ms} end,
   ["s1"]= function() close_scan_relay("S1"); return {["next"]= "r1", ["delay"]= 32*ms} end,
   ["s0"]= function() close_scan_relay("S0"); return {["next"]= "r0", ["delay"]= 32*ms} end,

   ["r8"]= function() read_relay_row("S8"); return {["next"]= "s7", ["delay"]= 32*ms} end,
   ["r7"]= function() read_relay_row("S7"); return {["next"]= "s6", ["delay"]= 32*ms} end,
   ["r6"]= function() read_relay_row("S6"); return {["next"]= "s5", ["delay"]= 32*ms} end,
   ["r5"]= function() read_relay_row("S5"); return {["next"]= "s4", ["delay"]= 32*ms} end,
   ["r4"]= function() read_relay_row("S4"); return {["next"]= "s3", ["delay"]= 32*ms} end,
   ["r3"]= function() read_relay_row("S3"); return {["next"]= "s2", ["delay"]= 32*ms} end,
   ["r2"]= function() read_relay_row("S2"); return {["next"]= "s1", ["delay"]= 32*ms} end,
   ["r1"]= function() read_relay_row("S1"); return {["next"]= "s0", ["delay"]= 32*ms} end,
   ["r0"]= function() read_relay_row("S0"); return {["next"]= "release", ["delay"]= 32*ms} end,
   ["transmit"] = state_transmit,
   ["transmit_wait"] = state_transmit_wait,
   ["release"] = state_release,
}

cur_state = "start"
trouble_type = nil
trouble = {}

function tick()
   cb = state[cur_state]
   ret = cb()
   delay = (ret["delay"] or 100*ms)
   cur_state = ret["next"]
   if (cur_state ~= "idle") then
      print("registering for entry into state [", cur_state, "] after ", delay)
   end
   t_tick:register(delay, tmr.ALARM_SINGLE, tick)
   t_tick:start()
end
   

setup_leads()
restore_leads()

t_tick = tmr.create()
t_tick:register(10000, tmr.ALARM_SINGLE, tick)
t_tick:start()

