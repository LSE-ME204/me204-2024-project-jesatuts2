# The gymternet: an exploration of toepoint, artistry, and drama

### About me

Hello. My name is Jes Hyne. For the past my whole life, I have been intrigued and captivated by the skill, strength, and fearlessness of women artistic gymnasts (the men, I'm sure, are very talented also). Sadly, we only really get an opportunity to watch the gymnastics once every four years, at the Olympics. More motivated gymnastics fans can find their way the yearly World Championships, but this is not nearly enough to scratch the itch.
 
When I learned of NCAA gymnastics tournament in the USA, I was thrilled. They still use the 10.0 system! Perfection is achievable! Go you go for a team without uncomfortable nationalistic implications! The code of points is slightly easier than in the elite competitions, resulting in cleaner, more precisely executed skills. Pointed toes! Oversplits! Stuck landings!

![Can you see getting jazzed for something like this? Katelyn Ohashi performs a sky-high switch split jump directly into splits](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2N3MzE2NWp0OTZoZDFrczE5N21idWJ3OGdiN3Uwbm13MWNpZ29meiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g4IP1VnrIUNRxKygV6/giphy.webp)

Because of the general high standard across the board, week after week during the season, scores pour in and it's hard to really determine who is relatively good and who is bad. When I was a kid, anything over an 8.0 was good and a 9.0 was incredible. In this tournament, among the top teams, it seems like a 9.7 or lower is reserved for routines with an obvious error, and the teams should only really be happy with a 9.8 or higher.

With all this score bunching, how can we tell the good from the great? And more importantly, how can I use this information to make predictions and win fame and admiration among a niche internet community? 

Well, for the last two years, I have been painstakingly manually collecting, inputting, and analysing data from live score sheets into my own database. I live near the *beach*. These events happen in the *morning*. In *summer*. On the *weekend*. I can't be spending my life typing little numbers into little boxes. It's repetitive, requires precision, and follows some fairly strict protocol to get the job done. This is the sort of work that machines love the way I love going to the beach on a summer morning. It's time to delegate.

### The Data: 

[Road to Nationals (RTN)]('https://roadtonationals.com/results/index.php') started off as some gymnerds' project to make gymnastics scores data more accessible to the community, and has since been adopted as the official statistical site of NCAA Gymnastics, and have been providing tools for coaches, athletes, and fans ever since.

Typically, live scores are published using one of several platforms, typically per a license held by the university hosting the meet. After the meet, scores are validated by the judges and coaches, and only then are they published to RTN. So RTN is not only the most official, but most complete respository for this data.

I chose to analyse data over the past 10 years. This was arbitrary, and I noticed that the RTN website struggled with retrieving some of the older data, so I just drew a line where I thought I would have plenty of data, but not too much issue in the supply chain.

The structure of the RTN website is very tidy; the front page gives you the internal reference numbers for each team, which in turn can lead you to the team's dashboard. The team's dashboard gives you the internal reference number for each meet, which in turn can lead you to the url for the meet dashboard. The meet dashboard gives you information about the scores and the gymnasts' performance; the units of analysis I am most interested in.

<figure>
![Navigating around the RTN website. URL slugs point to internal references to teams, meets, and years.](https://github.com/user-attachments/assets/297ddf3f-de9e-48e5-9bd7-17b9cd82d35f)  
<figcaption>Navigating around the RTN website. URL slugs point to internal references to teams, meets, and years..</figcaption>
</figure>

As a consequence of this intuitive web structure, I started off scraping directly using Scrapy; using the slugs from the `<a>` tags to get the next set of links to scrape from. This became very slow, very fast. RTN has a lovely interface, but the pages load s l o w l y. This wasn't working.

When I became aware of the hidden api structure within the site, I was back in business. I could navigate around the website using the same principles (using the team ids, meet ids and years to form curls to feed into my hungry scraping machine).


### Key Findings: 

#### Tenniest apparatus

***Setting the scene:*** **Imagine I'm a NCAA college gymnast, and I think it might feel good a 10 every once in a while. Where should I focus my training?**

There is a truism in elite gymnastics that states that the less gymnastics you do, the higher you will score. We saw this play out over the 2020/1 Olympic Games, with Olympic All-Round gold-medallist Sunisa Lee dropping elements of her routines that were attracting more execution deductions than they were contributing to her overall difficulty value. Evidentally, it paid off.

NCAA doesn't have a separate difficulty score, so it ought to follow that doing the least number of elements would result in a higher chance of getting a perfect 10.0. That is, it should be considerably easier to achieve a 10 on Vault (where the gymnast only has to perform one element) than any of the other events (where a gymnast has to perform at least 8 elements)

But what do we have here?

<iframe src="figures/01.%20tenniest_apparatus_ever.html" title="Tenniest apparatus ever" width="800" height="400"></iframe>

The data show that there is no major difference between apparatus in terms of what I'm dubbing *tenniness*.

We can see that the slices per year have some more meaningful differences in them, so I broke them down into a little animation to explore what I like to think of as trends in perceiving perfection over the years. In the last two seasons, we can see both the quantity of 10s overall has increased dramatically, and judges seem to be favouring floor exercise for leniency.

<iframe src="figures/02.%20tenniest_apparatus_per_year.html" title="Tenniest apparatus per year" width="800" height="450"></iframe>

#### Tenniest teams

***Setting the scene:*** **Imagine I'm a prospective NCAA college gymnast, and I think it might feel good a 10 every once in a while. Which colleges should I consider attending?**

Which teams have been the most successful at ~~bribing the judges~~ performing perfect gymnastics? Georgia and Alabama have legacies of dominance, but most recently Oklahoma has been the most dominant team. 

In the meantime, fans complain that in recent years judges are increasingly prepared to award a 10 for excellent (if imperfect) routines. What do the data say?

<iframe src="figures/03.%20tenniest_teams_ever.html" title="Tenniest teams ever" width="800" height="600"></iframe>
<sup> *Scroll to see* </sup>

No surprises here; Oklahoma dominates this analysis. However, the relatively poor perfomance of Alabama and Georgia is somewhat surprising. Could it be that history didn't start in 2015 and their dominance pre-dates this analysis? Scientists will never know.

What about specialist schools? Recently, Utah is known for their wonderful beam rotation, and Cal has excellent bars workers. Are they excellent enough to show up in the disaggregated data?

<iframe src="figures/04.%20tenniest_teams_per_apparatus.html" title="Tenniest apparatus per apparatus" width="800" height="600"></iframe>
<sup> *Scroll to see* </sup>

And what if we want to compare some teams head-to-head, apparatus-by-apparatus? We can do that too.

<iframe src="figures/05.%20tenniest_teams_per_apparatus_per_year" title="Tenniest teams per apparatus per year" width="800" height="1200"></iframe>

### Future: 
I'd like to next dig into the data about the gymnasts themselves. Who are some of the greatest GOATS of all time*? For each apparatus? Which teams do they prefer?

I'd like to do some analysis on the average and median scores of gymnasts, as this is, in my view, a better predictor of their overall performance than their capability to get a 10.

Eventually, I'd like to build a small tool that uses indicators like performance frequency, average or median score, and other factors that might impact performance that aren't currently captured in my data (home or away might factor, judging panels might factor, proximity to mid-terms might factor, etc).

Finally, I'd like to integrate the tools and skills I have built doing this assignment into my existing rails gymternet project, and buy myself some beach-time. If my fantasy team wins next year, I'll buy you a beer.

There's a real potential to stir up some good gossip if I am able to integrate some information I already have about the judges into this data and find some patterns and (we secretly hope) *corruption*. Or unconscious bias, whatever. Nobody seems to be really tracking that sort of information and there's nothing a gymfan likes more than complaining about the judges. *What if we could evidence our whingeing?* That's the dream.

![That's me out](https://i0.wp.com/balancebeamsituation.com/wp-content/uploads/2022/02/curtissalute.gif?resize=474%2C305&ssl=1)
