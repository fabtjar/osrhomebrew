const FORM_SETS = document.getElementById('formsets');
const TOTAL_FORMS = getTotalForms();
let total_forms_count = parseInt(TOTAL_FORMS.value);

function addEmptyForm() {
    const div = document.createElement('div');
    div.classList.add('multiField');
    div.innerHTML += EMPTY_FORM.replaceAll('__prefix__', TOTAL_FORMS.value);
    FORM_SETS.appendChild(div);

    total_forms_count++;
    TOTAL_FORMS.value = total_forms_count.toString();
}

function getTotalForms() {
    const fields = FORM_SETS.getElementsByTagName('input');
    for (let i = 0; i < fields.length; i++) {
        const field = fields[i];
        if (field.name.includes('TOTAL_FORMS'))
            return field;
    }
}
