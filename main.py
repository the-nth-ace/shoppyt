from typing import List
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello world"

    @strawberry.field
    def all_fields(self) -> List[str]:
        return ["1", "2"]


schema = strawberry.Schema(Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
