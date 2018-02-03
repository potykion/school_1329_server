from django.test.client import encode_multipart

from school_1329_server.schedule.models import ScheduleSubject
from tests.schedule.setup import ScheduleFixtures
from tests.users.setup import UsersFixtures


class TestSubjectsViews(ScheduleFixtures, UsersFixtures):
    def test_list_subjects(
            self, client, user_token,
            subject
    ):
        """
        Given subject,
        When list subjects,
        Then response contains subjects.
        """
        response = client.get('/api/schedule_subjects', **user_token)

        assert response.data == [
            {
                'id': subject.pk,
                'title': subject.title
            }
        ]

    def test_subject_create(
            self, client, user_token,
    ):
        """
        Given subject title,
        When create subject with given title,
        Then subject is created,
        And response contains new subject info.
        """
        subject_title = 'ЯРусский'
        response = client.post('/api/schedule_subjects', {
            'title': subject_title
        }, **user_token)

        subject = ScheduleSubject.objects.get(title=subject_title)
        assert subject.pk
        assert response.data == {
            'title': subject_title,
            'id': subject.pk
        }

    def test_subject_delete(
            self, client, user_token,
            subject
    ):
        """
        Given subject,
        When delete subject,
        Then no subjects exists.
        """
        response = client.delete(f'/api/schedule_subjects/{subject.pk}', **user_token)

        assert response.status_code == 200
        assert not ScheduleSubject.objects.filter(pk=subject.pk).exists()

    def test_subject_update(
            self, client, user_token,
            subject
    ):
        """
        Given subject,
        And new subject title,
        When update subject,
        Then subject is updated,
        And response contains new subject info.
        """
        subject_title = 'ЯРусский'

        boundary_string = 'BoUnDaRyStRiNg'
        encoded_data = encode_multipart(boundary_string, {'title': subject_title})
        content_type = f'multipart/form-data; boundary={boundary_string}'

        response = client.put(
            f'/api/schedule_subjects/{subject.pk}',
            encoded_data,
            **user_token,
            content_type=content_type
        )

        assert ScheduleSubject.objects.get(pk=subject.pk).title == subject_title
        assert response.data == {
            'title': subject_title,
            'id': subject.pk
        }
