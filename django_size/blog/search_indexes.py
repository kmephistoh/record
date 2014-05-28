from blog.models import Article
from haystack import indexes

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):  
    text = indexes.CharField(document=True, use_template=True)      

    def get_model(self):  
        return Article
    def index_queryset(self, using=None):  
        """Used when the entire index for model is updated."""    
        return self.get_model().objects.all()
