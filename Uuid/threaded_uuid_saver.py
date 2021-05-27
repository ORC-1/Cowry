from Uuid.model_files.uuid_model import Uuid


def t_uuid_saver(**kwargs):
    try:
        uuid_saved = Uuid.objects.create(
            value=kwargs.get('value')
        )
        if uuid_saved:
            print('t_uuid_saver saving done...')
        else:
            print('t_uuid_saver saving done...')

    except Exception as e:
        print("Error at t_uuid_saver: ", str(e))
