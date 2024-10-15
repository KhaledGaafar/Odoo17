odoo.define('digizilla.button', function (require) {
    "use strict";

    var FormController = require('web.FormController');
    
    FormController.include({
        _onButtonClicked: function (event) {
            if (event.data.attrs.name === "create") {
                event.stopPropagation();
            } else {
                this._super(event);
            }
        }
    });
});
