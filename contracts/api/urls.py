from django.urls import include, path

from .views import ClaimList, ClaimCreate, ClaimReadUpdateDelete, ClientList, \
    ClientCreate, ClientSearch, ClientReadUpdateDelete, CompanyList, \
    CompanyCreate, CompanySearch, CompanyReadUpdateDelete, ContractList, \
    ContractCreate, ContractReadUpdateDelete, ManufacturerList, \
    ManufacturerCreate, ManufacturerReadUpdateDelete, ProductList, \
    ProductCreate, ProductReadUpdateDelete, RegionList, RegionCreate, \
    RegionReadUpdateDelete, ShipmentList, ShipmentCreate, \
    ShipmentReadUpdateDelete

urlpatterns = [
    # auth urls
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),

    # claim urls
    path("claim/list", ClaimList.as_view()),
    path("claim/create", ClaimCreate.as_view()),
    path("claim/<int:pk>", ClaimReadUpdateDelete.as_view()),

    # client urls
    path("client/list", ClientList.as_view()),
    path("client/create", ClientCreate.as_view()),
    path("client/search", ClientSearch.as_view()),
    path("client/<int:pk>", ClientReadUpdateDelete.as_view()),

    # company urls
    path("company/list", CompanyList.as_view()),
    path("company/create", CompanyCreate.as_view()),
    path("company/search", CompanySearch.as_view()),
    path("company/<int:pk>", CompanyReadUpdateDelete.as_view()),

    # contract urls
    path("contract/list", ContractList.as_view()),
    path("contract/create", ContractCreate.as_view()),
    path("contract/<int:pk>", ContractReadUpdateDelete.as_view()),

    # manufacturer urls
    path("manufacturer/list", ManufacturerList.as_view()),
    path("manufacturer/create", ManufacturerCreate.as_view()),
    path("manufacturer/<int:pk>", ManufacturerReadUpdateDelete.as_view()),

    # product urls
    path("product/list", ProductList.as_view()),
    path("product/create", ProductCreate.as_view()),
    path("product/<int:pk>", ProductReadUpdateDelete.as_view()),

    # region urls
    path("region/list", RegionList.as_view()),
    path("region/create", RegionCreate.as_view()),
    path("region/<int:pk>", RegionReadUpdateDelete.as_view()),

    # shipment urls
    path("shipment/list", ShipmentList.as_view()),
    path("shipment/create", ShipmentCreate.as_view()),
    path("shipment/<int:pk>", ShipmentReadUpdateDelete.as_view()),
]
