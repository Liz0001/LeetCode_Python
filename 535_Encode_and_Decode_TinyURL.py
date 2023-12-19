import unittest
import uuid


class Codec:
    short = {}
    long = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        
        if longUrl not in self.long:
            id = str(uuid.uuid4())[:6]
            s = "http://tinyurl.com/"+id
            self.long[longUrl] = s
            self.short[s] = longUrl
            return "http://tinyurl.com/"+id
        else:
            return self.long[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        
        if shortUrl not in self.short:
            return ""
        else:
            return self.short[shortUrl]
    

class TestCodec(unittest.TestCase):
    """535. Encode and Decode TinyURL."""

    def test_encode(self):
        c = Codec()
        url = "https://leetcode.com/problems/design-tinyurl"
        exp = "https://leetcode.com/problems/design-tinyurl"
        out = c.decode(c.encode(url))
        self.assertEqual(out, exp)
    
        
if __name__ == '__main__':
    unittest.main()
