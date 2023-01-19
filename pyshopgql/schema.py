import graphene

from catalog.schema import CatalogQuery


class Query(CatalogQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
