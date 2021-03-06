from fastapi import APIRouter
from justwatch import JustWatch

movie = APIRouter()

justwatch = JustWatch(country="UY")

all_providers = justwatch.get_providers()

icon_base_url = "https://images.justwatch.com"


@movie.get("/movies/providers/{name}", tags=["Movies"])
def get_providers(name: str):
    # Busco pelicula por el nombre
    # TODO: Agregar mas especificidad al buscar la pelicula. Ej: año, id, etc.
    movie = justwatch.search_for_item(query=name)
    # Uso función search_providers para obtener los proveedores de la pelicula
    result = {"message": "", "providers": {}}

    if  len(movie["items"]) > 0 and "offers" in movie["items"][0]:
        result["message"] = "Proveedores encontrados correctamente."
        result["providers"] = search_providers(movie["items"][0]["offers"])
    else:
        result["message"] = "No se encontraron películas con ese nombre o no tiene proveedores."

    return result

def search_providers(movie_providers):
    providers = {}
    # Recorro los proveedores de la pelicula y el array con todos los proveedores de justwatch
    for offer in movie_providers:
        for provider in all_providers:
            # Si los id's coinciden y no existe ese id en el diccionario
            if offer["provider_id"] == provider["id"] and not provider["id"] in providers:
                # Agrego item al diccionario identificado por el id del proveedor
                # con nombre de proveedor, url de la pelicula y el icono
                providers[provider["id"]] = {
                    "name": provider["clear_name"],
                    "movie_url": offer["urls"]["standard_web"],
                    "icon_url": icon_base_url + provider["icon_url"].format(profile="s100"),
                    "icon_blur_hash": provider["icon_blur_hash"]}
    return providers
