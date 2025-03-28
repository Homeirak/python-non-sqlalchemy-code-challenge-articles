class Article:
    
    all = []

    def __init__(self, author, magazine, title):

        self.author = author
        self.magazine = magazine
        
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
            Article.all.append(self)
        else:
            raise Exception("Title must be a string between 5 and 50 characters")
        

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "_title"):
            return
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            raise Exception("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author class")
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine class")

class Author:
    all = []
    def __init__(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise Exception("Name must be a non-empty string")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            return
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise Exception("Name must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:
    
    all = []
    
    def __init__(self, name, category):
        # self.name = name
        
        if type(name) == str and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 characters")

        if type(category) == str and len(name) >0:
            self._category = category
        else:
            raise Exception("Name must be a non-empty string")
        
        Magazine.all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 2 <= len(new_name) <= 16:
            self._name = new_name
        # else:
        #     raise Exception("Name must be a string between 2 and 16 characters")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if type(new_category) == str and len(new_category) >0:
            self._category = new_category
        # else:
        #     raise Exception("Name must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)