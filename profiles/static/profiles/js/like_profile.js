$(document).ready(function(){
    $('.favourite-profile').click(
        function(e) {
            let profile_id = $(this).attr('data-profile-item');
            let that = $(this);
            let icon = that.find('.fa-heart');
            let icon_classlist_value = icon[0].classList.value;
            let csrftoken = Cookies.get('csrftoken');
            let action_url = `${profile_id}/add-to-favourite/`;

            $.ajax({
                url: action_url,
                type: 'POST',
                data: {'attr_id': product_id, 'icon_classlist_value': icon_classlist_value },
                headers : {'X-CSRFToken': csrftoken},
                success: function (result) {
                    if (icon[0].classList.contains('fa-regular')) {
                        icon[0].classList.remove('fa-regular');
                        icon[0].classList.add('fa-solid');
                    } else if (icon[0].classList.contains('fa-solid')) {
                        icon[0].classList.remove('fa-solid');
                        icon[0].classList.add('fa-regular');
                    }
                },   
            });
        }
    );
});