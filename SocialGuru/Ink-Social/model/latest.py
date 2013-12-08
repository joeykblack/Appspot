'''
Created on Jun 1, 2012

@author: joey
'''

class LatestMixin(object):
    """A mixin for db.Model objects that will add a `latest` method to the
    `Query` object returned by cls.all(). Requires that the ORDER_FIELD
    contain the name of the field by which to order the query to determine the
    latest object."""

    # What field do we order by?
    ORDER_FIELD = None

    @classmethod
    def all(cls):
        # Get the real query
        q = super(LatestMixin, cls).all()
        # Define our custom latest method
        def latest():
            if cls.ORDER_FIELD is None:
                raise ValueError('ORDER_FIELD must be defined')
            return q.order('-' + cls.ORDER_FIELD).get()
        # Attach it to the query
        q.latest = latest
        return q
