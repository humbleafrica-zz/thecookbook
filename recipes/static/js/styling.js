// Material Design example
$(document).ready(function() {
    $('#dtBasic ').DataTable();
    $('#dtBasic_wrapper').find('label').each(function() {
        $(this).parent().append($(this).children());
    });
    $('#dtBasic_wrapper .dataTables_filter').find('input').each(function() {
        $('input').attr("placeholder", "Search");
        $('input').removeClass('form-control-sm');
    });
    $('#dtBasic_wrapper .dataTables_length').addClass('d-flex flex-row');
    $('#dtBasic_wrapper .dataTables_filter').addClass('md-form');
    $('#dtBasic_wrapper select').removeClass(
        'custom-select custom-select-sm form-control form-control-sm');
    $('#dtBasic_wrapper select').addClass('mdb-select');
    $('#dtBasic_wrapper .mdb-select').dtBasic();
    $('#dtBasic_wrapper .dataTables_filter').find('label').remove();

    $('.dataTables_length').addClass('bs-select');

    /*built in form render styling*/
    $(
        "#id_username, #id_password1, #id_password2, #id_name, #id_serves, #id_method, #id_prep_time, #id_cook_time, #id_description, #id_ingredients, #id_instructions, #id_suits, #id_calories, #id_fat, #id_saturates, #id_carbs, #id_sugars, #id_fibre, #id_protein, #id_salt, #id_publisher, #id_allergy, #id_difficulty, #id_recipe_type, #id_cuisine, #id_published_date, #id_uploaded_date, #id_update, #id_image, #id_notes"
    ).addClass("frow");

    $('form p').addClass(
        'col'
    );

    $('#id_username, #id_password1, #id_password2').addClass(
        'row'
    );
});
