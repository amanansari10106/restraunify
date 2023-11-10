


def subDomainForWebsiteRender(fulldoamin):
    check = ".localhost" in fulldoamin
    subDomain = fulldoamin.split(".")
    if check and len(subDomain)==2:
        return subDomain
    return False

