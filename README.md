# RUNNN 
> **A Psychological Survival Horror Game Where The Rules Change**  
> *MADE BY VPS*  
> 
>  **Play Online Directly in Browser:** [https://vansh-vps.github.io/TRIAL/](https://vansh-vps.github.io/TRIAL/)

---

##  Table of Contents
- [About the Game](#-about-the-game)
- [The "Curious Thing" in this Game](#-the-curious-thing-in-this-game)
- [ How to Play](#-how-to-play)
  - [Core Objectives](#core-objectives)
  - [Items & Mechanics](#items--mechanics)
- [ Controls](#️-controls)
- [ Game Modes](#-game-modes)
- [ Survival Tips & Strategies](#-survival-tips--strategies)
- [ How to Run the Game](#-how-to-run-the-game)
- [ Credits & Attribution](#-credits--attribution)

---

##  About the Game

**RUNNN** is a tense, atmospheric retro top-down pixel horror game set inside a subterranean, decaying industrial facility. You play as an isolated maintenance worker surviving night shifts in a dark maze of rusty corridors, conveyor belts, generators, and a colossal central furnace.

Stalking the corridors is a relentless entity known as **Cobb**. Your job is to keep the facility operational by completing critical maintenance tasks while staying one step ahead of the creature in the dark.

---

##  The "Curious Thing" in this Game

Most horror games adhere to fixed rules: the monster has a set detection radius, moves at a predictable speed, and follows consistent behavioral logic.

**In RUNNN, the fundamental laws of reality mutate every shift.**

The game's defining hook is its **Dynamic Rule Shifting System** (`constants.json`): before each night begins (or whenever you press `TAB`), the game assigns a new combination of **Monster Rules** and **Player Rules**. A strategy that kept you alive on Night 1 could get you killed in seconds on Night 2.

###  Monster Rules (Cobb's Mutating Senses)
* **`monster.see` (Cobb can See)**: Light becomes your worst enemy. If you step under lamps or carry a lit candle within Cobb's line of sight, he will immediately charge. You must navigate using dark corners and shadows.
* **`monster.hear` (Cobb can Hear)**: Sound travels across the bunker. Sprinting or flipping loud circuit breakers will alert Cobb across rooms. You can pick up and throw **rocks** to generate noise elsewhere and lure him away.
* **`monster.smell` (Cobb can Smell)**: Cobb tracks your scent trail. You cannot hide behind walls or in dark corners. As he closes in, you will hear his horrifying sniffing audio cue grow louder. Constant movement and distance management are your only defense.
* **`monster.duplicate` (Cobb Duplicates)**: A single creature is no longer your only problem. Multiple copies of Cobb roam the corridors simultaneously, cutting off escape routes and flanking you.
* **`monster.reach` (Cobb can Reach)**: Cobb sprouts horrifying elongated limbs, allowing him to grab you from a distance and snatch you around tight corridor corners.

###  Player Rules (Your Personal Afflictions)
* **`you.freeze` (Freezing Cold)**: A **Freeze Meter** appears on screen. The facility temperature drops to sub-zero levels. If the meter empties, you freeze to death. You must periodically return to the warm central furnace or carry a lit candle to stay warm.
* **`you.starve` (Starvation)**: A **Hunger Meter** appears on screen. Your body exhausts its energy rapidly. You must explore the dark maze to scavenge for carrots growing through facility cracks to keep yourself fed before starving.

---

##  How to Play

### Core Objectives
Each shift presents a checklist of industrial maintenance tasks displayed in the bottom status panel:
1. **Deliver Coal (`Deliver Coal X/Y`)**:
   - Locate chunks of coal on conveyor belts or on the ground.
   - Carry them back to the central furnace and feed the flames to prevent facility blackout.
2. **Flip Breakers (`Flip Breakers X/Y`)**:
   - Search the labyrinthine corridors for electrical breaker boxes.
   - Interact with them to restore power. *Be careful:* resetting a breaker sounds a loud buzzer across the complex!
3. **Insert Batteries**:
   - Retrieve industrial batteries and seat them into designated sockets to power up doors and machinery.
4. **Survive the Night**:
   - Evade Cobb, monitor your vitals (freeze/hunger if active), and reach the shift quota to progress.

### Items & Mechanics
| Item / Object | Appearance | Function |
| :--- | :--- | :--- |
| **Coal** | Black rock chunk | Feeds the central furnace to keep the heat and power alive. |
| **Candle** | Small burning candle | Portable heat source. Prevents freezing during `you.freeze` shifts (but exposes your position if `monster.see` is active!). |
| **Rock** | Small grey pebble | Throwable projectile. Impacts create sound distractions to misdirect Cobb during `monster.hear` shifts. |
| **Carrot** | Orange vegetable | Consumable food. Staves off death during `you.starve` shifts (carrots respawn over time). |
| **Battery** | Yellow/green cylinder | Restores auxiliary generator circuits. |
| **Breaker** | Wall-mounted switch | Resets electrical power for facility zones. |
| **Conveyor Belts** | Moving conveyor tiles | Automatically transport coal and items across rooms. |

---

##  Controls

Fully supports both **Keyboard & Mouse** and **Gamepad**:

| Action | Keyboard / Mouse | Gamepad |
| :--- | :--- | :--- |
| **Move** | `W`, `A`, `S`, `D` or Arrow Keys | Left Analog Stick / D-Pad |
| **Sprint / Run** | `Left Shift` | `RB` / `R1` (Right Shoulder) |
| **Interact / Pick Up / Eat / Fuel** | `E` or `Spacebar` / `Enter` | `A` (Xbox) / `Cross` (PlayStation) |
| **Throw Rock (Distraction)** | `F` or `Left Mouse Click` | `X` (Xbox) / `Square` (PlayStation) |
| **View Shift Rules (Manifesto)** | `TAB` | `Y` (Xbox) / `Triangle` (PlayStation) |
| **Pause / Resume** | `P` or `Escape` | `Start` / `Options` |

---

##  Game Modes

* **Story Mode**:
  - The progressive campaign featuring escalating difficulty, shifting rule sets each night, and persistent save data.
  - Culminates in an intense **Game Finale** showdown involving the industrial Blast Furnace.
* **Endless Mode**:
  - Unlocked procedural survival mode starting at Level 3 difficulty.
  - Survive unlimited waves of randomized rule mutations to achieve a personal best high score.
* **Level Select**:
  - Allows you to replay any unlocked shift to test different survival strategies under specific rule constraints.

---

##  Survival Tips & Strategies

1. **Check the Rules Immediately (`TAB`)**:
   - Always press `TAB` at the start of a shift to see what Cobb can do and whether you need to manage hunger or temperature.
2. **The Candle Dilemma**:
   - If both `you.freeze` and `monster.see` are active, holding a candle prevents freezing but turns you into a beacon. Only hold the candle until your Freeze bar recovers, then drop it to hide in shadows.
3. **Use Noise as a Weapon**:
   - When `monster.hear` is on, Cobb responds aggressively to breaker alarms. Carry a rock with you: the moment you flip a breaker, throw the rock in the opposite direction to lure Cobb away from your escape route.
4. **Listen for the Sniffing**:
   - If `monster.smell` is active, stereo audio is crucial. When Cobb's sniffing grows loud in your headphones, stop what you are doing and relocate immediately.
5. **Carrots Respawn**:
   - If you are starving, remember that eaten carrots eventually regrow in their original locations. Keep a mental map of carrot patches.

---


---

##  Credits & Attribution

* **Recreation & Enhancements**: MADE BY VPS
* **Original Game & Concept**: Winner of **Major Jam 7**
  - **abho**: Art, Animation, Programming, Game Design
  - **Vystel**: Programming (Enemy AI, Game Mechanics)
  - **Federico Calchera**: Programming (Map Generation, Quality of Life)
  - **frost**: Sound Effects, Ambience
  - **Jimmy**: Music, Ambience
