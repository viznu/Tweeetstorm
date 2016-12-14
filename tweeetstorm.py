import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
 
  terrorism = ['Account','Acid','Advance','Aerial','Agency','Aggression','Aggressor','Agitator','Aim','Aircraft','Airfield','Airplane','Airport','Alarm','Alert','Alliance','Allies','Ambush','Ammunition','Anarchy','Anguish','Annihilate','Apartheid','Appeasement','Armament','Armed forces','Armory','Arms','Arsenal','Artillery','Ashore','Assassin','Assassinate','Assault','Atrocity','Attack','Attrition','Authority','Automatic','Tactics','Tank','Target','Tension','Terrain','Terror','Terrorism','Terrorist','Terrorize','Threat','Threaten','Thwart','Topple','Torch','Torpedo','Tourniquet','Tragic','Training','Trample','Transportation','Trap','Trauma','Treachery','Trench','Trigger','Triumph','Turbulent','Machine guns','Machines','Maim','Malevolent','Malicious','Maraud','March','Massacre','Mayhem','Megalomania','Menace','Method','Militancy','Militant','Militaristic','Military','Militia','Mines','Missile','Mission','Mistreatment','Mobile','Mobilization','Momentum','Mortars','Munitions','Murder','Muscle']

  haxxor = [
"abbrev", "ABEND", "accumulator", "ACK", "ad-hockery", "Ada", "adger", "admin", "ADVENT", "AFJ", "AI", "koans", 
"AI-complete", "AIDS", "AIDX", "airplane", "rule", "aliasing", "bug", "all-elbows", "alpha", "particles", "alt"
, "alt", "bit", "altmode", "Aluminum", "Book", "amoeba", "amp", "off", "amper", "angle", "brackets", "angry",
"fruit", "salad", "annoybot", "AOS", "app", "arc", "arc", "wars", "archive", "arena", "arg", "armor-plated", 
"asbestos", "asbestos", "cork", "award", "asbestos", "longjohns", "ASCII", "ASCII", "art", "attoparsec", 
"autobogotiphobia", "automagically", "avatar", "awk", "back door", "backbone cabal", "backbone site", 
"backgammon", "background", "BAD", "Bad Thing", "bag on the side", "bagbiter", 
"bamf", "banana label", "banana problem", "bandwidth", 
"bang", "bang on", "bang path", "banner", "bar", "bare metal", "barf", 
"barfmail", "barfulation", "barfulous", "barney", "baroque", "BartleMUD", "BASIC", "batch", "bathtub curve", 
"baud", "baud barf", "baz", "bboard", "BBS", "beam", 
"beanie key", "beep", "benchmark", "Berkeley Quality Software", "berklix", "berserking", "Berzerkeley", 
"beta", "BFI", "bible", "BiCapitalization", "BIFF", "BIFF", "Big Gray Wall", "big iron", "Big Red Switch", 
"big win", "big-endian", "bignum", "bigot", "bit", "bit bang", "bit bashing", "bit bucket", "bit decay", "bit rot", 
"bit twiddling", "bit-paired keyboard", "bitblt", "BITNET", "bits", "bitty box", "bixie", "black art", "black hole", 
"black magic", "blargh", "blast", "blat", "bletch", "bletcherous", "blinkenlights", "blit", "blitter", 
"blivet", "BLOB", "block", "block transfer computations", "blow an EPROM", "blow away", "blow out", "blow past"]


  scam = ["buttons-for-website.com","7makemoneyonline.com","darodar.com","semalt.com","ilovevitaly.co","myftpupload.com","econom.co","iskalko.ru","ilovevitaly.ru","ilovevitaly.com","o-o-8-o-o.ru","o-o-6-o-o.ru","cenoval.ru","priceg.com","cenokos.ru","seoexperimenty.ru","gobongo.info","vodkoved.ru","adcash.com","websocial.me","cityadspix.com","luxup.ru","ykecwqlixx.ru","superiends.org","slftsdybbg.ru","edakgfvwql.ru","socialseet.ru","screentoolkit.com","savetubevideo.com","blackhatworth.com","prlog.ru","hulfingtonpost.com","bestwebsitesawards.com","forum.smailik.org","social-buttons.com","simple-share-buttons.com","aliexpress.com","googlsucks.com","theguardlan.com","4webmasters.org","Get-Free-Traffic-Now.com"]


  profanity =  [       "Chutiya", "Randi" , "maader chod" , "chodu" 
 ]

  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "laqkbHrYXN6r8HSipI6xNKCWP",
    "consumer_secret"     : "HLBxNVpW4v5ahLIMRqVuaPchMlKXUhZgCcIemJal0D39SjuWjI",
    "access_token"        : "797589780599083008-ZMRx3i8Ry9zrbdfkeF3D4v6iPzE3mKD",
    "access_token_secret" : "xeE3HQLhwhQB4IUksHnM86iMMIetA9RCqm8AOncJkDMjb" 
    }

  api = get_api(cfg)

  for i in profanity:
  	tweet = i
  	status = api.update_status(status=tweet) 

  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
