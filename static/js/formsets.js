const FORM_SETS = document.getElementById('formsets');
const TOTAL_FORMS = getFormData('TOTAL_FORMS');
const MAX_NUM_FORMS_COUNT = getFormData('MAX_NUM_FORMS').value;
const FORMSET_ADD_BUTTON = document.getElementById('add-special-attack-button');

let total_forms_count = parseInt(TOTAL_FORMS.value);

FORMSET_ADD_BUTTON.addEventListener('click', () => addEmptyForm());

function addEmptyForm() {
    const div = document.createElement('div');
    div.classList.add('multiField');
    div.innerHTML += EMPTY_FORM.replaceAll('__prefix__', TOTAL_FORMS.value);
    FORM_SETS.appendChild(div);

    total_forms_count++;
    TOTAL_FORMS.value = total_forms_count.toString();

    if (TOTAL_FORMS.value >= MAX_NUM_FORMS_COUNT)
        checkButtonDisabled();
}

function checkButtonDisabled() {
    if (TOTAL_FORMS.value >= MAX_NUM_FORMS_COUNT)
        FORMSET_ADD_BUTTON.classList.add('disabled');
}

checkButtonDisabled();

function getFormData(name) {
    const fields = FORM_SETS.getElementsByTagName('input');
    for (let i = 0; i < fields.length; i++) {
        const field = fields[i];
        if (field.name.includes(name))
            return field;
    }
}
