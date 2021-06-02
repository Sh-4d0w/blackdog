import requests
import ipaddress


class Ipverse:
    """
        A class to represent a IPBlocks.
        ...

        Attributes
        ----------
        country : str
            country abbreviation
        _url : str
            site url

        Methods
        -------
        get_all_ranger_by_country():
            returns the country IP block list
        """
    def __init__(self,country):
        """
        country : str
            country abbreviation
        _url : str
            site url
        """
        self._url = "http://ipverse.net/ipblocks/data/countries/"
        self.country = country

    def get_all_ranger_by_country(self):
        """
        returns the country IP block list
        :return: list
        """
        countryIpv4List = []
        r = requests.get(self._url + self.country.lower() + ".zone")
        for cidr in r.text.splitlines():
            if not cidr.startswith("#"):
                countryIpv4List.append(ipaddress.ip_network(cidr, False))
        return countryIpv4List

