//IE8 polyfill
var isArray = Array.isArray || function (arr) {
    return Object.prototype.toString.call(arr) == '[object Array]';
};
var costs = {
    "ddnet": [145, 145, "Silex"], // nfoservers.com
    "ger": [170, 170, "Shishigami"], // nfoservers.com
    "ger2": [20, 20, "Learath2"], // hetzner.de
    "fra": [66, 66, "heinrich5991"], // soyoustart.com
    "rus": [33, 48, "KOMПOT"], // ihor.ru
    "chl": 85, // zglobalhost.com
    "bra": "RafaelFF",
    "zaf": 65, // clickworks.co.za
    "usa": [72, 72, "heinrich5991"], // nfoservers.com
    "can": "o_tee_one",
    "chn": "Tom",
};
var donated = 401;
var old = 2304;

var sum = 0;
var sumToPay = 0;
var sumPartSponsored = 0;
var num = 0
for (var server in costs) {
    if (costs.hasOwnProperty(server)) {
        var val = costs[server];
        if (val.toFixed) {
            sum += val;
            sumToPay += val;
            num += 1;
        } else if (isArray(val)) {
            sum += val[1];
            sumToPay += val[1] - val[0];
            sumPartSponsored += val[0];
            num += 1;
        }
    }
}

var donatedRest = 0;
var paid = {};
for (var server in costs) {
    if (costs.hasOwnProperty(server)) {
        var val = costs[server];
        paid[server] = 0;
        if (donatedRest > 0) {
            paid[server] += donatedRest;
        }
        if (val.toFixed) {
            paid[server] += val * donated / sumToPay;
            if (paid[server] > val) {
                donatedRest += paid[server] - val;
                paid[server] = val;
            }
        } else if (isArray(val)) {
            paid[server] += (val[1] - val[0]) * donated / sumToPay + val[0];
            if (paid[server] > val[1]) {
                donatedRest += paid[server] - val[1];
                paid[server] = val[1];
            }
        } else {
        }
    }
}

var total = donated + sumPartSponsored;
var rest = 1540;
if (total > sum) {
    rest += total - sum;
    total = sum;
}
var elements = [];
var value = 100 * total / sum;
var color = '#F6A828';
if (total >= sum) {
    color = '#37d628';
}
elements = document.querySelectorAll("#funding-total");
elements.forEach(function (element, index, array) {
    element.className += " ui-progressbar ui-widget ui-widget-content ui-corner-all";
    element.insertAdjacentHTML("beforeend", '<div class="ui-progressbar-value ui-widget-header ui-corner-left' + (value == 100 ? " ui-corner-right" : "") + '" style="width: ' + (value).toFixed(0) + '%; background: ' + color + ';"></div>');
});
elements = document.querySelectorAll("#funding-total .progress-label");
elements.forEach(function (element, index, array) {
    if (element.textContent !== undefined)
        element.textContent = total.toFixed() + " € donated / " + sum + " € cost 2018";
    else
        element.innerText = total.toFixed() + " € donated / " + sum + " € cost 2018";
});
elements = document.querySelectorAll("#funding-total .ui-widget-header");
elements.forEach(function (element, index, array) {
    element.style.backgroundColor = color;
});

for (var server in costs) {
    if (costs.hasOwnProperty(server)) {
        var val = costs[server];
        var value = 0;
        var text = '';
        var color = '#F6A828';
        if (val.toFixed) {
            value = 100 * paid[server] / val;
            text = (paid[server]).toFixed() + " / " + val + " €";
            if (paid[server] >= val) {
                color = '#37d628';
            }
        } else if (isArray(val)) {
            value = 100 * paid[server] / val[1];
            text = (paid[server]).toFixed() + " / " + val[1] + " €";
            if (paid[server] >= val[1]) {
                color = '#37d628';
            }
            if (val.length > 2) {
                text += " (sponsored by " + val[2] + ")";
            }
        } else {
            value = 100;
            text = "sponsored by " + val;
            color = '#37d628';
        }
        elements = document.querySelectorAll("#funding-" + server);
        elements.forEach(function (element, index, array) {
            element.className += " ui-progressbar ui-widget ui-widget-content ui-corner-all";
            element.insertAdjacentHTML("beforeend", '<div class="ui-progressbar-value ui-widget-header ui-corner-left' + (value == 100 ? " ui-corner-right" : "") + '" style="width: ' + (value).toFixed(0) + '%; background: ' + color + ';"></div>');
        });
        elements = document.querySelectorAll("#funding-" + server + " .progress-label");
        elements.forEach(function (element, index, array) {
            if (element.textContent !== undefined)
                element.textContent = text;
            else
                element.innerText = text;
        });
    }
}

var value = 100 * rest / old;
color = '#F6A828';
if (rest >= old) {
    color = '#37d628';
}
elements = document.querySelectorAll("#funding-old");
elements.forEach(function (element, index, array) {
    element.className += " ui-progressbar ui-widget ui-widget-content ui-corner-all";
    element.insertAdjacentHTML("beforeend", '<div class="ui-progressbar-value ui-widget-header ui-corner-left' + (value == 100 ? " ui-corner-right" : "") + '" style="width: ' + (value).toFixed(0) + '%; background: ' + color + ';"></div>');
});
elements = document.querySelectorAll("#funding-old .progress-label");
elements.forEach(function (element, index, array) {
    if (element.textContent !== undefined)
        element.textContent = rest.toFixed() + " € / " + old + " € cost 2013-17";
    else
        element.innerText = rest.toFixed() + " € / " + old + " € cost 2013-17";
});
