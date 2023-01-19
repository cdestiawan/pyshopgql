import graphene
from graphene_django import DjangoObjectType

from .models import Category, Product, ProductImage


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductImage(DjangoObjectType):
    class Meta:
        model = ProductImage


class CatalogQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)
    get_product_by_slug = graphene.Field(
        ProductType, slug=graphene.String(required=True))
    get_category_by_slug = graphene.Field(
        ProductType, slug=graphene.String(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_get_product_by_slug(root, info, slug):
        try:
            return Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return None

    def resolve_get_category_by_slug(root, info, slug):
        try:
            return Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return None
