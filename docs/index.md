#The gymternet

#An exploration of toepoint, artistry, and drama

##About me

Hello. My name is Jes Hyne. For the past my whole life, I have been intrigued and captivated by the skill, strength, and fearlessness of women artistic gymnasts (the men, I'm sure, are very talented also). Sadly, we only really get an opportunity to watch the gymnastics once every four years, at the Olympics. More motivated gymnastics fans can find their way the yearly World Championships, but this is not nearly enough to scratch the itch.
 
When I learned of NCAA gymnastics tournament in the USA, I was thrilled. They still use the 10.0 system! Perfection is achievable! Go you go for a team without uncomfortable nationalistic implications! The code of points is slightly easier than in the elite competitions, resulting in cleaner, more precisely executed skills. Pointed toes! Oversplits! Stuck landings!

Because of the general high standard across the board, week after week during the season, scores pour in and it's hard to really determine who is relatively good and who is bad. When I was a kid, anything over an 8.0 was good and a 9.0 was incredible. In this tournament, among the top teams, it seems like a 9.7 or lower is reserved for routines with an obvious error, and the teams should only really be happy with a 9.8 or higher.

With all this score bunching, how can we tell the good from the great? And more importantly, how can I use this information to make predictions and win fame and admiration among a niche internet community? 

Well, for the last two years, I have been painstakingly manually collecting, inputting, and analysing data from live score sheets into my own database. I live near the *beach*. These events happen in the *morning*. In *summer*. On the *weekend*. I can't be spending my life typing little numbers into little boxes. It's repetitive, requires precision, and follows some fairly strict protocol to get the job done. This is the sort of work that machines love the way I love going to the beach on a summer morning. It's time to delegate.

##The Data: 

[Road to Nationals (RTN)]('https://roadtonationals.com/results/index.php') started off as some gymnerds' project to make gymnastics scores data more accessible to the community, and has since been adopted as the official statistical site of NCAA Gymnastics, and have been providing tools for coaches, athletes, and fans ever since.

Typically, live scores are published using one of several platforms, typically per a license held by the university hosting the meet. After the meet, scores are validated by the judges and coaches, and only then are they published to RTN. So RTN is not only the most official, but most complete respository for this data.

I chose to analyse data over the past 10 years. This was arbitrary, and I noticed that the RTN website struggled with retrieving some of the older data, so I just drew a line where I thought I would have plenty of data, but not too much issue in the supply chain.

The structure of the RTN website is very tidy; the front page gives you the internal reference numbers for each team, which in turn can lead you to the team's dashboard. The team's dashboard gives you the internal reference number for each meet, which in turn can lead you to the url for the meet dashboard. The meet dashboard gives you information about the scores and the gymnasts' performance; the units of analysis I am most interested in.

<iframe src="https://github.com/LSE-ME204/me204-2024-project-jesatuts2/blob/main/docs/notes/RTN_sml.gif"></iframe>

As a consequence of this intuitive web structure, I started off scraping directly using Scrapy; using the slugs from the `<a>` tags to get the next set of links to scrape from. This became very slow, very fast. RTN has a lovely interface, but the pages load s l o w l y. This wasn't working.

When I became aware of the hidden api structure within the site, I was back in business. I could navigate around the website using the same principles (using the team ids, meet ids and years to form curls to feed into my hungry scraping machine).


#Key Findings: 

What are the main insights you gained from your data? What are the most interesting things you found? Something like “Once I cleaned up the data by doing X, Y and Z, I found that the price of bread in the UK has increased by 20% in the last 5 years while the price of milk has remained stable, as shown in the plot below” would be a good example.

<iframe src="https://github.com/LSE-ME204/me204-2024-project-jesatuts2/blob/main/docs/figures/tenniest_apparatus_animation.html"></iframe>

#Future: 
What would you do next if you had more time? What other questions could you ask of this data? What other data sources could you use to complement this data?
