def get_profile(model):
    try:
        profile = model.objects.get()

    except model.DoesNotExist as ex:
        return

    return profile


def disable_fields(form):
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
