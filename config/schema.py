import strawberry
from rooms import schema as rooms_schema


# urls.py, views.py
@strawberry.type
class Query(rooms_schema.Query):
    pass


@strawberry.type
class Mutation(rooms_schema.Mutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
