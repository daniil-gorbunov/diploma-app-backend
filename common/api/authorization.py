from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class AllowAllAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return object_list

    def read_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return True

    def create_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return object_list

    def create_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return True

    def update_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return object_list

    def update_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")
        return True

    def delete_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")