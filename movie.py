from dataclasses import dataclass

@dataclass
class Movie:
    title: str        
    year: int         
    director: str     
    genre: str        
    rating: float = 0.0  
    
    def __str__(self):
        return f"{self.title} ({self.year}), реж. {self.director}"