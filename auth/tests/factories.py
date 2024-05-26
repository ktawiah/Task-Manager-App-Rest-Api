import factory
from faker import Faker
from auth.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        skip_postgeneration_save = True

    id = factory.LazyFunction(fake.uuid4)
    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    last_name = factory.LazyFunction(fake.last_name)
    email = factory.LazyFunction(fake.unique.email)

    @factory.post_generation
    def password(self, created, extracted, **kwargs):
        if created:
            return
        elif extracted:
            self.set_password(extracted)
        else:
            self.set_password(fake.password())
