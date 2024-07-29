![01  tenniest_apparatus_ever](https://github.com/user-attachments/assets/96e406bb-ce27-4fd5-bcda-59edf03067ef)# The gymternet: an exploration of toepoint, artistry, and drama

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

![Navigating around the RTN website. URL slugs point to internal references to teams, meets, and years.](https://github.com/user-attachments/assets/297ddf3f-de9e-48e5-9bd7-17b9cd82d35f)
As a consequence of this intuitive web structure, I started off scraping directly using Scrapy; using the slugs from the `<a>` tags to get the next set of links to scrape from. This became very slow, very fast. RTN has a lovely interface, but the pages load s l o w l y. This wasn't working.

When I became aware of the hidden api structure within the site, I was back in business. I could navigate around the website using the same principles (using the team ids, meet ids and years to form curls to feed into my hungry scraping machine).


### Key Findings: 

There is a truism in elite gymnastics that states that the less gymnastics you do, the higher you will score. We saw this play out over the 2020/1 Olympic Games, with Olympic All-Round gold-medallist Sunisa Lee dropping elements of her routines that were attracting more execution deductions than they were contributing to her overall difficulty value. Evidentally, it paid off.

NCAA doesn't have a separate difficulty score, so it ought to follow that doing the least number of elements would result in a higher chance of getting a perfect 10.0. That is, it should be considerably easier to achieve a 10 on Vault (where the gymnast only has to perform one element) than any of the other events (where a gymnast has to perform at least 8 elements)

But what do we have here?
![Uploading 01. ten<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" display="block" class="plt-container" width="600.0" height="400.0">
  <style type="text/css">
  .plt-container {
   font-family: Lucida Grande, sans-serif;
   user-select: none;
   -webkit-user-select: none;
   -moz-user-select: none;
   -ms-user-select: none;
}
text {
   text-rendering: optimizeLegibility;
}
#pAWlPCg .plot-title {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 16.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .plot-subtitle {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 15.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .plot-caption {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .legend-title {
   fill: #474747;
   font-family: Helvetica;
   font-size: 12.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .legend-item {
   fill: #474747;
   font-family: Helvetica;
   font-size: 10.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .axis-title-x {
   fill: #474747;
   font-family: Helvetica;
   font-size: 12.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .axis-text-x {
   fill: #474747;
   font-family: Helvetica;
   font-size: 12.0px;
   font-weight: normal;
   font-style: normal;   
}
#d2KJwrn .axis-tooltip-text-x {
   fill: #ffffff;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .axis-title-y {
   fill: #474747;
   font-family: Helvetica;
   font-size: 12.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .axis-text-y {
   fill: #474747;
   font-family: Helvetica;
   font-size: 12.0px;
   font-weight: normal;
   font-style: normal;   
}
#d2KJwrn .axis-tooltip-text-y {
   fill: #ffffff;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .facet-strip-text-x {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#pAWlPCg .facet-strip-text-y {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#d2KJwrn .tooltip-text {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: normal;
   font-style: normal;   
}
#d2KJwrn .tooltip-title {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: bold;
   font-style: normal;   
}
#d2KJwrn .tooltip-label {
   fill: #474747;
   font-family: Lucida Grande, sans-serif;
   font-size: 13.0px;
   font-weight: bold;
   font-style: normal;   
}

  </style>
  <g id="pAWlPCg">
    <path fill-rule="evenodd" fill="rgb(255,255,255)" fill-opacity="1.0" d="M0.0 0.0 L0.0 400.0 L600.0 400.0 L600.0 0.0 Z">
    </path>
    <g transform="translate(26.5 26.5 ) ">
      <g>
        <g transform="translate(28.100138184373485 0.0 ) ">
          <g>
            <line x1="81.4616070186412" y1="0.0" x2="81.4616070186412" y2="282.0" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="206.7871562780892" y1="0.0" x2="206.7871562780892" y2="282.0" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="332.11270553753724" y1="0.0" x2="332.11270553753724" y2="282.0" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="457.43825479698523" y1="0.0" x2="457.43825479698523" y2="282.0" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
          </g>
        </g>
        <g transform="translate(28.100138184373485 0.0 ) ">
          <g>
            <line x1="0.0" y1="282.0" x2="538.8998618156265" y2="282.0" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="0.0" y1="214.85714285714286" x2="538.8998618156265" y2="214.85714285714286" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="0.0" y1="147.71428571428572" x2="538.8998618156265" y2="147.71428571428572" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="0.0" y1="80.57142857142858" x2="538.8998618156265" y2="80.57142857142858" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
            <line x1="0.0" y1="13.428571428571445" x2="538.8998618156265" y2="13.428571428571445" stroke="rgb(233,233,233)" stroke-opacity="1.0" stroke-width="1.0" fill="none">
            </line>
          </g>
        </g>
      </g>
      <g clip-path="url(#cnWEd5J)" clip-bounds-jfx="[rect (28.100138184373485, 0.0), (538.8998618156265, 282.0)]">
        <g transform="translate(28.100138184373485 0.0 ) ">
          <g>
            <g>
              <rect x="401.0417576302336" y="13.428571428571445" height="69.15714285714284" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(253,231,37)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="82.58571428571429" height="42.97142857142859" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(181,222,43)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="125.55714285714288" height="51.69999999999999" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(108,205,90)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="177.25714285714287" height="14.099999999999994" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(53,183,121)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="191.35714285714286" height="2.6857142857142833" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(31,158,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="194.04285714285714" height="37.599999999999994" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(38,130,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="231.64285714285714" height="16.114285714285728" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(49,104,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="247.75714285714287" height="10.742857142857133" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(62,74,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="258.5" height="18.80000000000001" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(72,40,120)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="401.0417576302336" y="277.3" height="4.699999999999989" width="112.79299433350326" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(68,1,84)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="14.100000000000023" height="46.32857142857142" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(253,231,37)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="60.428571428571445" height="84.6" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(181,222,43)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="145.02857142857144" height="25.514285714285705" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(108,205,90)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="170.54285714285714" height="13.428571428571445" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(53,183,121)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="183.9714285714286" height="21.485714285714266" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(31,158,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="205.45714285714286" height="5.371428571428567" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(38,130,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="210.82857142857142" height="35.58571428571429" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(49,104,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="246.4142857142857" height="23.5" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(62,74,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="269.9142857142857" height="10.742857142857133" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(72,40,120)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="275.71620837078564" y="280.65714285714284" height="1.3428571428571558" width="112.7929943335032" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(68,1,84)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="18.80000000000001" height="37.599999999999994" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(253,231,37)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="56.400000000000006" height="54.3857142857143" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(181,222,43)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="110.7857142857143" height="30.885714285714272" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(108,205,90)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="141.67142857142858" height="29.542857142857144" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(53,183,121)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="171.21428571428572" height="6.714285714285722" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(31,158,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="177.92857142857144" height="25.514285714285705" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(38,130,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="203.44285714285715" height="34.24285714285713" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(49,104,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="237.68571428571428" height="17.457142857142856" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(62,74,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="255.14285714285714" height="5.371428571428595" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(72,40,120)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="150.3906591113376" y="260.51428571428573" height="21.485714285714266" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(68,1,84)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="27.52857142857144" height="30.214285714285722" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(253,231,37)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="57.74285714285716" height="59.08571428571429" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(181,222,43)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="116.82857142857145" height="39.6142857142857" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(108,205,90)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="156.44285714285715" height="33.571428571428584" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(53,183,121)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="190.01428571428573" height="18.799999999999983" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(31,158,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="208.81428571428572" height="20.814285714285717" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(38,130,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="229.62857142857143" height="6.714285714285722" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(49,104,142)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="236.34285714285716" height="14.771428571428572" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(62,74,137)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="251.11428571428573" height="8.05714285714285" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(72,40,120)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
              <rect x="25.065109851889595" y="259.1714285714286" height="22.828571428571422" width="112.79299433350323" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(68,1,84)" fill-opacity="0.8" stroke-width="0.44000000000000006">
              </rect>
            </g>
          </g>
        </g>
        <defs>
          <clipPath id="cnWEd5J">
            <rect x="28.100138184373485" y="0.0" width="538.8998618156265" height="282.0">
            </rect>
          </clipPath>
        </defs>
      </g>
      <g>
        <g transform="translate(28.100138184373485 282.0 ) ">
          <g transform="translate(81.4616070186412 0.0 ) ">
            <line stroke-width="1.0" stroke="rgb(71,71,71)" stroke-opacity="1.0" x2="0.0" y2="4.0">
            </line>
            <g transform="translate(0.0 7.0 ) ">
              <text class="axis-text-x" text-anchor="middle" dy="0.7em">
                <tspan>Vault</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(206.7871562780892 0.0 ) ">
            <line stroke-width="1.0" stroke="rgb(71,71,71)" stroke-opacity="1.0" x2="0.0" y2="4.0">
            </line>
            <g transform="translate(0.0 7.0 ) ">
              <text class="axis-text-x" text-anchor="middle" dy="0.7em">
                <tspan>Uneven Bars</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(332.11270553753724 0.0 ) ">
            <line stroke-width="1.0" stroke="rgb(71,71,71)" stroke-opacity="1.0" x2="0.0" y2="4.0">
            </line>
            <g transform="translate(0.0 7.0 ) ">
              <text class="axis-text-x" text-anchor="middle" dy="0.7em">
                <tspan>Balance Beam</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(457.43825479698523 0.0 ) ">
            <line stroke-width="1.0" stroke="rgb(71,71,71)" stroke-opacity="1.0" x2="0.0" y2="4.0">
            </line>
            <g transform="translate(0.0 7.0 ) ">
              <text class="axis-text-x" text-anchor="middle" dy="0.7em">
                <tspan>Floor Exercise</tspan>
              </text>
            </g>
          </g>
          <line x1="0.0" y1="0.0" x2="538.8998618156265" y2="0.0" stroke-width="1.0" stroke="rgb(71,71,71)" stroke-opacity="1.0">
          </line>
        </g>
        <g transform="translate(28.100138184373485 0.0 ) ">
          <g transform="translate(0.0 282.0 ) ">
            <g transform="translate(-3.0 0.0 ) ">
              <text class="axis-text-y" text-anchor="end" dy="0.35em">
                <tspan>0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(0.0 214.85714285714286 ) ">
            <g transform="translate(-3.0 0.0 ) ">
              <text class="axis-text-y" text-anchor="end" dy="0.35em">
                <tspan>100</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(0.0 147.71428571428572 ) ">
            <g transform="translate(-3.0 0.0 ) ">
              <text class="axis-text-y" text-anchor="end" dy="0.35em">
                <tspan>200</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(0.0 80.57142857142858 ) ">
            <g transform="translate(-3.0 0.0 ) ">
              <text class="axis-text-y" text-anchor="end" dy="0.35em">
                <tspan>300</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(0.0 13.428571428571445 ) ">
            <g transform="translate(-3.0 0.0 ) ">
              <text class="axis-text-y" text-anchor="end" dy="0.35em">
                <tspan>400</tspan>
              </text>
            </g>
          </g>
        </g>
      </g>
    </g>
    <g transform="translate(54.600138184373485 16.8 ) ">
      <text class="plot-title" y="0.0">
        <tspan>Which apparatus attracts the most 10s in NCAA gymnastics?</tspan>
      </text>
    </g>
    <g transform="translate(13.600000000000001 167.5 ) rotate(-90.0 ) ">
      <text class="axis-title-y" y="0.0" text-anchor="middle">
        <tspan>No. of Tens</tspan>
      </text>
    </g>
    <g transform="translate(324.05006909218673 350.6 ) ">
      <text class="axis-title-x" y="0.0" text-anchor="middle">
        <tspan>Apparatus</tspan>
      </text>
    </g>
    <g transform="translate(-12.245665557296263 357.0 ) ">
      <rect x="5.0" y="5.0" height="33.0" width="662.591469298966" stroke="rgb(71,71,71)" stroke-opacity="1.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
      </rect>
      <g transform="translate(10.0 10.0 ) ">
        <g transform="translate(0.0 15.100000000000001 ) ">
          <text class="legend-title" y="0.0">
            <tspan>Season</tspan>
          </text>
        </g>
        <g transform="translate(45.9236207265035 0.0 ) ">
          <g transform="">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(68,1,84)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2015.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(60.66678485724625 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(72,40,120)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2016.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(121.3335697144925 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(62,74,137)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2017.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(182.00035457173874 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(49,104,142)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2018.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(242.667139428985 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(38,130,142)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2019.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(303.33392428623125 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(31,158,137)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2020.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(364.0007091434775 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(53,183,121)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2021.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(424.6674940007237 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(108,205,90)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2022.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(485.33427885796993 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(181,222,43)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2023.0</tspan>
              </text>
            </g>
          </g>
          <g transform="translate(546.0010637152162 0.0 ) ">
            <g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke-width="0.0" fill="rgb(255,255,255)" fill-opacity="1.0">
              </rect>
              <g transform="translate(1.0 1.0 ) ">
                <g>
                  <rect x="0.0" y="0.0" height="21.0" width="21.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" fill="rgb(253,231,37)" fill-opacity="1.0" stroke-width="1.5">
                  </rect>
                </g>
              </g>
              <rect x="0.0" y="0.0" height="23.0" width="23.0" stroke="rgb(255,255,255)" stroke-opacity="1.0" stroke-width="1.0" fill-opacity="0.0">
              </rect>
            </g>
            <g transform="translate(26.069463636718538 15.0 ) ">
              <text class="legend-item" y="0.0">
                <tspan>2024.0</tspan>
              </text>
            </g>
          </g>
        </g>
      </g>
    </g>
    <path fill="rgb(0,0,0)" fill-opacity="0.0" stroke="rgb(71,71,71)" stroke-opacity="1.0" stroke-width="0.0" d="M0.0 0.0 L0.0 400.0 L600.0 400.0 L600.0 0.0 Z">
    </path>
  </g>
  <g id="d2KJwrn">
  </g>
</svg>niest_apparatus_ever.svg…]()

![A plot comparing the total number of 10s achieved across all apparatus from 2015-2024](https://github.com/LSE-ME204/me204-2024-project-jesatuts2/blob/main/docs/figures/01.%20tenniest_apparatus_ever.svg)

The data show that there is no major difference between apparatus in terms of what I'm dubbing *tenniness*.

We can see that the slices per year have some more meaningful differences in them, so I broke them down into a little animation to explore what I like to think of as trends in perceiving perfection over the years. In the last two seasons, we can see both the quantity of 10s overall has increased dramatically, and judges seem to be favouring floor exercise for leniency.

![A plot comparing the total number of 10s achieved across all apparatus from 2015-2024](https://github.com/LSE-ME204/me204-2024-project-jesatuts2/blob/main/docs/figures/01.%20tenniest_apparatus_ever.svg)

What are the main insights you gained from your data? What are the most interesting things you found? Something like “Once I cleaned up the data by doing X, Y and Z, I found that the price of bread in the UK has increased by 20% in the last 5 years while the price of milk has remained stable, as shown in the plot below” would be a good example.

<iframe src="https://github.com/LSE-ME204/me204-2024-project-jesatuts2/blob/main/docs/figures/tenniest_apparatus_animation.html"></iframe>

### Future: 
What would you do next if you had more time? What other questions could you ask of this data? What other data sources could you use to complement this data?
