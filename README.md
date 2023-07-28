# Is Alcaraz a mix of Novak Djokovic, Rafael Nadal and Roger Federer ? 

After his loss at Wimbledon final, Novak Djokovic described Carlos Alcaraz as ‘basically the best’ mix of himself, Rafael Nadal and Roger Federer: [watch Djokovic statement](https://www.youtube.com/shorts/Jx4dHZQzDV0). 

As Data science nerds, we wanted to analyze this statement from a statistical point of view. The aim of this project is 
to create a skills profile for each tennis player and look for similarities between players. 

We used the data from [tennisabstract.com](https://tennisabstract.com/), big thanks to Jeff Sackmann for his great work!

# Creating a tennis player profile

Based on the data available on [tennisabstract.com](https://tennisabstract.com/), we defined the following tennis profile:
- Serve (for 1st serve and 2nd serve separately)
    - Unret%:  Unreturnable percentage. The percentage of a player’s serves that don’t come back, whether an ace, a service winner, or a return error.
    - <=3 W%: Percent of service points won on either the serve or second shot.
    - SvImpact – Serve Impact. A stat invented by Jeff Sackmann, to measure how much the serve influences points won even when the return comes back (see [glossary](http://www.tennisabstract.com/blog/2019/08/17/match-charting-project-serve-stats-glossary/)).

- Return (for 1st and 2nd serve return separately)
    - RiP%: Return in play percentage. The percent of return points in which this player got the serve back in play.
    - RetWnr%: Return winner percentage. The percentage of return points in which the return was a winner (or induced a forced error).

- Forehand 
    - Wnr FH%: Return winner forehand percentage.
    - FH Wnr%: Forehand winner percentage. The percentage of topspin forehands (excluding forced errors) that result in winners or induced forced errors.
    - FH DTL Wnr%: Forehand down-the-line winning percentage.
    - Forehand inside-out winning percentage. 

- Backhand
    - BH Wnr%: Backhand winner percentage. 
    - BH DTL Wnr%: Backhand down-the-line winner percentage.

- Volley
    - Net W%: Net point winning percentage. The percentage of net points won by this player.
    - Net Freq: Net point frequency. The percentage of total points in which the player comes to net, including serve-and-volley points.

- Drop shots
    - Drop Freq: Dropshot frequency. The percentage of groundstrokes that are dropshots. 
    - Drop Wnr%: Dropshot winner percentage.

- Agressivity
    - SnV Freq%: Serve-and-volley frequency.
    - SnV W%: Serve-and-volley winning percentage.