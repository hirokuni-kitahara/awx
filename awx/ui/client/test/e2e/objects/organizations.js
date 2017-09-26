import breadcrumb from './sections/breadcrumb.js';
import createFormSection from './sections/createFormSection.js';
import header from './sections/header.js';
import lookupModal from './sections/lookupModal.js';
import navigation from './sections/navigation.js';
import pagination from './sections/pagination.js';
import permissions from './sections/permissions.js';
import search from './sections/search.js';

const details = createFormSection({
    selector: 'form',
    props: {
        formElementSelectors: [
            '#organization_form input.Form-textInput',
            '#organization_form .Form-lookupButton',
            '#organization_form #InstanceGroups'
        ]
    }
});

module.exports = {
    url() {
        return `${this.api.globals.awxURL}/#/organizations`;
    },
    sections: {
        header,
        navigation,
        breadcrumb,
        lookupModal,
        add: {
            selector: 'div[ui-view="form"]',
            sections: {
                details
            },
            elements: {
                title: 'div[class^="Form-title"]'
            }
        },
        edit: {
            selector: 'div[ui-view="form"]',
            sections: {
                details,
                permissions
            },
            elements: {
                title: 'div[class^="Form-title"]'
            }
        },
        list: {
            selector: '#organizations',
            elements: {
                badge: 'span[class~="badge"]',
                title: 'div[class="List-titleText"]',
                add: 'button[class~="List-buttonSubmit"]'
            },
            sections: {
                search,
                pagination
            }
        }
    },
    elements: {
        cancel: 'button[class*="Form-cancelButton"]',
        save: 'button[class*="Form-saveButton"]'
    }
};
