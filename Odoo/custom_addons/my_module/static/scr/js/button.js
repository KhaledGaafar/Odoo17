odoo.define('digizilla.button', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if ($node) {
                $node.find('.o_form_button_create').hide();
            }
        },
    });
});
