(function () {
    // Source - https://stackoverflow.com/a/7220510
    // Posted by user123444555621, modified by community. See post 'Timeline' for change history
    // Retrieved 2026-03-20, License - CC BY-SA 3.0
    function syntaxHighlight(json) {
        json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
            var cls = 'number';
            if (/^"/.test(match)) {
                if (/:$/.test(match)) {
                    cls = 'key';
                } else {
                    cls = 'string';
                }
            } else if (/true|false/.test(match)) {
                cls = 'boolean';
            } else if (/null/.test(match)) {
                cls = 'null';
            }
            return '<span class="' + cls + '">' + match + '</span>';
        });
    }

    function resolveElement(elementOrId) {
        if (!elementOrId) {
            return null;
        }
        if (typeof elementOrId === 'string') {
            return document.getElementById(elementOrId);
        }
        return elementOrId;
    }

    function highlightPreformattedJson(elementOrId) {
        var jsonBlock = resolveElement(elementOrId);
        if (!jsonBlock) {
            return;
        }
        jsonBlock.innerHTML = syntaxHighlight(jsonBlock.textContent);
    }

    function renderPanel(panelOrId, cardData) {
        var panel = resolveElement(panelOrId);
        var jsonBlock;
        var emptyState;

        if (!panel) {
            return;
        }

        jsonBlock = panel.querySelector('.metadata-json');
        emptyState = panel.querySelector('.metadata-empty');

        if (!jsonBlock || !emptyState) {
            return;
        }

        if (!cardData) {
            jsonBlock.textContent = '';
            jsonBlock.innerHTML = '';
            jsonBlock.hidden = true;
            emptyState.hidden = false;
            return;
        }

        jsonBlock.textContent = JSON.stringify(cardData, null, 2);
        jsonBlock.hidden = false;
        emptyState.hidden = true;
        highlightPreformattedJson(jsonBlock);
    }

    function setPanelVisibility(panelOrId, isVisible) {
        var panel = resolveElement(panelOrId);
        if (!panel) {
            return;
        }
        panel.hidden = !isVisible;
    }

    window.CardMetadata = {
        highlightPreformattedJson: highlightPreformattedJson,
        renderPanel: renderPanel,
        setPanelVisibility: setPanelVisibility
    };
})();