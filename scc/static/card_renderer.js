(function () {
    var blankCardImage = null;
    var placeholderImage = null;
    var tooltipGridPromise = null;
    var tooltipGrid = null;
    var sharedTooltipElement = null;

    function ensureImage(src, cachedImage, callback) {
        if (cachedImage) {
            callback(cachedImage);
            return;
        }

        var img = new Image();
        img.onload = function () {
            callback(img);
        };
        img.src = src;
    }

    function ensureBlankCard(callback) {
        ensureImage('/blank-card', blankCardImage, function (img) {
            blankCardImage = img;
            callback(img);
        });
    }

    function ensurePlaceholder(callback) {
        ensureImage('/static/placeholder.png', placeholderImage, function (img) {
            placeholderImage = img;
            callback(img);
        });
    }

    function ensureTooltipGrid() {
        if (tooltipGrid) {
            return Promise.resolve(tooltipGrid);
        }
        if (!tooltipGridPromise) {
            tooltipGridPromise = fetch('/punch-tooltip-data')
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error('Unable to load punch tooltip data');
                    }
                    return response.json();
                })
                .then(function (data) {
                    tooltipGrid = data;
                    return data;
                })
                .catch(function (err) {
                    tooltipGridPromise = null;
                    throw err;
                });
        }
        return tooltipGridPromise;
    }

    function ensureTooltipElement() {
        var title;
        var description;

        if (sharedTooltipElement) {
            return sharedTooltipElement;
        }

        sharedTooltipElement = document.createElement('div');
        sharedTooltipElement.className = 'card-tooltip';
        sharedTooltipElement.setAttribute('aria-hidden', 'true');

        title = document.createElement('div');
        title.className = 'card-tooltip-title';
        sharedTooltipElement.appendChild(title);

        description = document.createElement('div');
        description.className = 'card-tooltip-description';
        sharedTooltipElement.appendChild(description);

        document.body.appendChild(sharedTooltipElement);
        return sharedTooltipElement;
    }

    function isPunchTooltipEnabled() {
        try {
            return localStorage.getItem('punchNameTooltips') === 'true';
        } catch (err) {
            return false;
        }
    }

    function createRenderer(options) {
        var settings = options || {};
        var canvasId = settings.canvasId || 'card';
        var geomId = settings.geomId || 'card-geom';
        var holeSize = settings.holeSize || 15;
        var geomElement = document.getElementById(geomId);
        var canvas = document.getElementById(canvasId);
        var geom = geomElement ? geomElement.dataset : {};
        var origX = parseFloat(geom.origX);
        var origY = parseFloat(geom.origY);
        var offX = parseFloat(geom.offX);
        var offY = parseFloat(geom.offY);
        var tooltipEnabled = settings.enablePunchTooltips !== false;
        var tooltipsAvailable = false;
        var tooltipElement = ensureTooltipElement();

        function hideTooltip() {
            tooltipElement.classList.remove('is-visible');
            tooltipElement.setAttribute('aria-hidden', 'true');
        }

        function positionTooltip(clientX, clientY) {
            var tooltipRect;
            var left = clientX + 16;
            var top = clientY + 16;
            var maxLeft;
            var maxTop;

            tooltipRect = tooltipElement.getBoundingClientRect();
            maxLeft = window.innerWidth - tooltipRect.width - 12;
            maxTop = window.innerHeight - tooltipRect.height - 12;
            if (left > maxLeft) {
                left = Math.max(12, clientX - tooltipRect.width - 16);
            }
            if (top > maxTop) {
                top = Math.max(12, clientY - tooltipRect.height - 16);
            }

            tooltipElement.style.left = left + 'px';
            tooltipElement.style.top = top + 'px';
        }

        function showTooltip(cellData, clientX, clientY) {
            var title = tooltipElement.querySelector('.card-tooltip-title');
            var description = tooltipElement.querySelector('.card-tooltip-description');
            var hasDescription = !!(cellData && cellData.description);

            if (!cellData || !cellData.name || cellData.name === '-') {
                hideTooltip();
                return;
            }

            title.textContent = cellData.name;
            description.textContent = hasDescription ? cellData.description : '';
            description.style.display = hasDescription ? 'block' : 'none';
            tooltipElement.classList.add('is-visible');
            tooltipElement.setAttribute('aria-hidden', 'false');
            positionTooltip(clientX, clientY);
        }

        function cellFromPointerEvent(event) {
            var rect;
            var intrinsicX;
            var intrinsicY;
            var minX;
            var minY;
            var col;
            var row;

            if (!tooltipsAvailable || !tooltipGrid) {
                return null;
            }

            rect = canvas.getBoundingClientRect();
            intrinsicX = (event.clientX - rect.left) * (canvas.width / rect.width);
            intrinsicY = (event.clientY - rect.top) * (canvas.height / rect.height) - 30; // adjust to align to tip of cursor
            minX = origX - (offX / 2);
            minY = origY - (offY / 2);
            col = Math.floor((intrinsicX - minX) / offX);
            row = Math.floor((intrinsicY - minY) / offY);

            if (row < 0 || col < 0 || row >= tooltipGrid.length || col >= tooltipGrid[row].length) {
                return null;
            }

            return tooltipGrid[row][col];
        }

        function handlePointerMove(event) {
            var cellData;

            if (!tooltipEnabled || !tooltipsAvailable || !isPunchTooltipEnabled()) {
                hideTooltip();
                return;
            }

            cellData = cellFromPointerEvent(event);
            if (!cellData) {
                hideTooltip();
                return;
            }

            showTooltip(cellData, event.clientX, event.clientY);
        }

        function drawImage(img) {
            var ctx = canvas.getContext('2d');
            canvas.width = img.naturalWidth;
            canvas.height = img.naturalHeight;
            ctx.drawImage(img, 0, 0);
            return ctx;
        }

        function renderPlaceholder() {
            tooltipsAvailable = false;
            hideTooltip();
            ensurePlaceholder(function (img) {
                drawImage(img);
            });
        }

        function renderCard(cardData) {
            try {
                ensureBlankCard(function (img) {
                    var ctx = drawImage(img);
                    var bits;
                    var xidx;
                    var yidx;
                    var cx;
                    var cy;

                    if (!cardData || !cardData.z_card) {
                        return;
                    }

                    bits = cardData.z_card;
                    tooltipsAvailable = true;
                    ctx.fillStyle = 'black';
                    for (xidx = 0; xidx < 69; xidx++) {
                        if (xidx > 30 && xidx < 38) {
                            continue;
                        }
                        for (yidx = 0; yidx < 18; yidx++) {
                            if (bits[yidx][xidx]) {
                                cx = origX + xidx * offX;
                                cy = origY + yidx * offY;
                                ctx.beginPath();
                                ctx.arc(cx, cy, holeSize, 0, Math.PI * 2);
                                ctx.fill();
                            }
                        }
                    }
                });
            } catch (err) {
                console.error('Error rendering card:', err);
                renderPlaceholder();
            }
        }

        if (tooltipEnabled) {
            ensureTooltipGrid().catch(function (err) {
                console.error('Error loading punch tooltip data:', err);
            });
            canvas.addEventListener('mousemove', handlePointerMove);
            canvas.addEventListener('mouseleave', hideTooltip);
        }

        return {
            renderCard: renderCard,
            renderPlaceholder: renderPlaceholder
        };
    }

    window.CardRenderer = {
        createRenderer: createRenderer
    };
})();