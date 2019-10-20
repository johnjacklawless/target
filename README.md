Hosted instance URL:
https://hwv85eqvwc.execute-api.us-east-2.amazonaws.com/dev/products/100000
https://hwv85eqvwc.execute-api.us-east-2.amazonaws.com/dev/products/100001

The crux of the problem is the URL mapping. Luckily, aws allows for a simple proxy, from there it's a single split.

I feel as if the bonus problem becomes trivial as the proxy method allows for a simple check of the method and boto is already setup.

I think this demostrates how microservices can significantly reduce the amount of code that needs to be written if the platform is feature complete. HA and horizontal scaling for ten lines of code? Seems like a pretty good deal.

That being said, the problem is incredably interesting but it mostly has to do with the real world challenge of implimenting the solution in open source, integrating with multiple ERPs//Inventory management tools, etc.
