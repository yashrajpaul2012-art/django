from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"he.html")
def monument(request):
    return render(request,"monument.html")
def cult(requests):
    return render(request, 'cult.html')
def festi(request):
    return HttpResponse("""<h1>Festivals of India: A Celebration of Culture and Diversity</h1>
<table style=border-width:1px::border-style:solid;border-colour:black;border-collapse:collapse></table>
<tr><th style=border-colour:black>India is a land of vibrant colors, diverse cultures, and rich traditions. One of the most striking reflections of this diversity is seen in its festivals. With every region, religion, and community adding their own flavor to celebrations, Indian festivals are a remarkable showcase of unity in diversity.</th>
Religious Festivals
Religious festivals form the core of Indian celebrations. These events are rooted in ancient traditions and mythology and are observed with great devotion and grandeur.

Diwali: Known as the Festival of Lights, Diwali is one of the most widely celebrated Hindu festivals. It marks the return of Lord Rama to Ayodhya and symbolizes the victory of light over darkness. People decorate their homes with lamps and rangoli, burst firecrackers, and .......
<a href="http://127.0.0.1:8000/cult/">Read More</a><th style=border-colour:black>
<img src="/static/festives.png" style=width:1000px;height:1000px>
</th>
</tr>
<a href="http://127.0.0.1:8000">Home page</a>""")
def indiagate(request):
    return render(request,"india gate.html")
def tajmahal(request):
    return HttpResponse("""
  <h1>Taj Mahal</h1>

  <div>
    <img src="/static/taj mahal.jpeg" alt="Taj Mahal" width="300">
  </div>
The Taj Mahal is perhaps the most recognized symbol of India. It is located in Agra, on the banks of the Yamuna River, in the state of Uttar Pradesh. Built by the Mughal emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal, it is a symbol of eternal love and devotion. Construction of the Taj Mahal began in 1632 and took about 22 years to complete, involving thousands of artisans and craftsmen from across the empire.

The Taj Mahal is made of white marble, brought in from Makrana in Rajasthan. Its architecture blends elements from Persian, Islamic, and Indian styles. The central dome rises to a height of about 73 meters, surrounded by four slender minarets. The entire structure is set within a vast complex that includes gardens, fountains, a mosque, and a guesthouse.

The walls of the Taj Mahal are decorated with precious stones, calligraphy from the Quran, and delicate floral carvings. The monument is especially breathtaking during sunrise and sunset when the marble reflects different shades of light. In 1983, it was designated a UNESCO World Heritage Site, and in 2007, it was included among the New Seven Wonders of the World.

Millions of visitors from around the world come to Agra each year to witness the magnificence of the Taj Mahal. Despite its age, the monument continues to inspire poets, artists, and travelers with its timeless beauty
<p><a href="http://127.0.0.1:8000/">HOME PAGE</a></p>""")
def redfort(request):
    return HttpResponse("""<h1>India Gate</h1>

  <div>
    <img src="/static/india gate.jpeg" alt="India Gate" width="300">
  </div>
The India Gate is a war memorial located in the center of New Delhi. Designed by the British architect Sir Edwin Lutyens, it was inaugurated in 1931. The structure is 42 meters high and resembles the Arc de Triomphe in Paris. It stands as a tribute to the 70,000 Indian soldiers who died during World War I, fighting for the British Indian Army.

Names of over 13,000 soldiers are inscribed on the walls of India Gate. Beneath the arch is the Amar Jawan Jyoti or “Flame of the Immortal Soldier,” which was added after the 1971 India-Pakistan war to honor unknown soldiers. A rifle with a soldier’s helmet stands on a black marble pedestal, and the flame burns continuously.

India Gate is not just a memorial but also a popular public space. Families, tourists, and locals visit the area, especially in the evenings, to enjoy the open space and fountains nearby. It is surrounded by lush green lawns and is part of the ceremonial axis of New Delhi, called the Rajpath.

India Gate represents the valor and sacrifice of Indian soldiers and stands tall as a symbol of national pride.


<p><a href=" http://127.0.0.1:8000/">HOME PAGE</a></p>""")