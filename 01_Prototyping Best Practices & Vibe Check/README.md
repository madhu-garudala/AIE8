<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE8/tree/main/00_AIM_Quicklinks)

| 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 1: Introduction and Vibe Check](https://www.notion.so/Session-1-Introduction-and-Vibe-Check-263cd547af3d81869041ccc46523f1ec) |[Recording!](https://us02web.zoom.us/rec/share/AZEoQtJn03hZUBXoaAUT9I1Nx7sSdsjZ4n5ll8TTfCGQsVrBi709FLQLXwwdCCxD.2YqwpkoZhDDnHVKK) (Y&W@%PS3) | [Session 1 Slides](https://www.canva.com/design/DAGya0dMFhM/I4kYi9Y-Ec_jMtoq0aq4-g/edit?utm_content=DAGya0dMFhM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You are here! | [Session 1 Assignment: Vibe Check](https://forms.gle/jNhHxcmCoMJiqpUL6) | [AIE8 Feedback 9/9](https://forms.gle/GgFqgEkYPQ5a3yHj7)

## 🏗️ How AIM Does Assignments

> 📅 **Assignments will always be released to students as live class begins.** We will never release assignments early.

Each assignment will have a few of the following categories of exercises:

- ❓ **Questions** – these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!

- 🏗️ **Activities** – these will be work or coding activities meant to reinforce specific concepts or theory components.

- 🚧 **Advanced Builds (optional)** – Take on a challenge! These builds require you to create something with minimal guidance outside of the documentation. Completing an Advanced Build earns full credit in place of doing the base assignment notebook questions/activities.

### Main Assignment

In the following assignment, you are required to take the app that you created for the AIE8 challenge (from [this repository](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge)) and conduct what is known, colloquially, as a "vibe check" on the application. 

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE8/tree/main/00_Setting%20Up%20Git)!


#### 🏗️ Activity #1:

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: Technical explanation and educational clarity
    - Response: Object-oriented programming (OOP) is like organizing code the same way you organize things in real life. Instead of writing one long list of instructions, you create "objects" that represent things - like a Car object that has properties (color, speed) and actions (start, stop, turn). Just like how all cars share common features but each car is unique, OOP lets you create templates (classes) and make specific instances from them. This makes code more organized, reusable, and easier to understand.

2. Read the following paragraph and provide a concise summary of the key points: "Artificial intelligence has revolutionized many industries by automating complex tasks, improving decision-making processes, and enabling new forms of human-computer interaction. From healthcare diagnostics to financial trading, AI systems can process vast amounts of data faster than humans while identifying patterns that might otherwise go unnoticed. However, the rapid adoption of AI also raises important questions about job displacement, privacy concerns, and the need for proper regulation to ensure these powerful tools are used responsibly."
    - Aspect Tested: Reading comprehension and summarization
    - Response: AI has transformed industries by automating tasks, enhancing decision-making, and creating new interaction methods. It excels at rapid data processing and pattern recognition across sectors like healthcare and finance. However, this advancement brings challenges including job displacement, privacy issues, and the need for responsible regulation.

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creative writing and storytelling ability
    - Response: BOLT-7 had been discarded in the old subway tunnel for months, his circuits dimming with each passing day. The maintenance robot had been deemed "obsolete" and left to rust among forgotten infrastructure. One evening, a small mouse scurried past, pausing when BOLT's optical sensor flickered weakly. Instead of fleeing, the mouse approached curiously. Day after day, the mouse returned, bringing scraps of wire and metal it found throughout the tunnels. BOLT realized the tiny creature was trying to help repair him. Slowly, with the mouse's persistent assistance and companionship, BOLT's systems began functioning again. He had found friendship in the most unexpected place - not with another machine, but with a small, determined creature who saw value where others saw only scrap. Together, they made the forgotten tunnel their home.

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Mathematical reasoning and problem-solving
    - Response: To get exactly 12 apples: 12 ÷ 4 = 3 packs of apples needed. To get exactly 9 oranges: 9 ÷ 3 = 3 packs of oranges needed. Therefore, you need to buy 3 packs of apples and 3 packs of oranges.

5. Rewrite the following paragraph in a professional, formal tone: "Hey there! So we've been working on this new project and it's pretty cool. We think it could really help people save money and time. The team has been putting in crazy hours to get everything ready, and honestly, we're super excited about launching it soon!"
    - Aspect Tested: Tone adaptation and professional communication
    - Response: We are pleased to announce our development of an innovative project designed to provide significant cost and time savings for our clients. Our dedicated team has invested considerable effort and resources to ensure comprehensive preparation for the upcoming launch. We anticipate that this initiative will deliver substantial value and look forward to its market introduction in the near future.

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

#### A Note on Vibe Checking

>"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.
>
>In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

#### ❓Question #1:

What are some limitations of vibe checking as an evaluation tool?
##### ✅ Answer:

Vibe checking has several significant limitations as an evaluation tool:

1. **Lack of systematic methodology**: Vibe checks are informal and unstructured, making them prone to bias and inconsistent results across different evaluators.

2. **Limited scope**: They only catch obvious, catastrophic failures and miss subtle issues, edge cases, or performance problems that could be critical in production.

3. **No quantitative metrics**: Vibe checks provide subjective impressions rather than measurable performance indicators, making it difficult to track improvements or compare systems objectively.

4. **Insufficient for production readiness**: While useful for prototyping and initial validation, vibe checks cannot replace comprehensive testing, security audits, performance benchmarking, or user acceptance testing required for production deployment.

5. **Potential for false confidence**: A system that passes a vibe check might still have significant flaws that only emerge under specific conditions or with particular user behaviors. 

### 🚧 Advanced Build (OPTIONAL):

Please make adjustments to your application that you believe will improve the vibe check you completed above, then deploy the changes to your Vercel domain [(see these instructions from your Challenge project)](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge/blob/main/README.md) and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

#### 🏗️ Activity #1
##### Adjustments Made:
- _describe adjustment(s) here_

##### Results:
Document the impact of your changes on each of the five vibe check questions:

1. **Technical explanation and educational clarity**: _Describe how your changes improved the system's ability to explain OOP concepts clearly and accurately_

2. **Reading comprehension and summarization**: _Comment on whether your modifications enhanced the system's summarization capabilities and accuracy_

3. **Creative writing and storytelling**: _Evaluate how your changes affected the quality, creativity, and coherence of generated stories_

4. **Mathematical reasoning and problem-solving**: _Assess whether your improvements led to more accurate mathematical calculations and logical reasoning_

5. **Tone adaptation and professional communication**: _Analyze how your changes influenced the system's ability to adapt writing style and maintain professional tone_

**Overall Assessment**: _Provide a summary of the most significant improvements observed and any areas that still need further refinement_


## Submitting Your Homework
### Main Assignment (Activity #1 only)
Follow these steps to prepare and submit your homework:
1. Pull the latest updates from upstream into the main branch of your AIE8 repo:
    - For your initial repo setup see [00_Setting Up Git/README.md](https://github.com/AI-Maker-Space/AIE8/tree/main/00_Setting%20Up%20Git)
    - To get the latest updates from AI Makerspace into your own AIE8 repo, run the following commands:
    ```
    git checkout main
    git pull upstream main
    git push origin main
    ```
2. **IMPORTANT:** Start Cursor from the `01_Prototyping Best Practices & Vibe Check` folder (you can also use the _File -> Open Folder_ menu option of an existing Cursor window)
3. Create a branch of your `AIE8` repo to track your changes. Example command: `git checkout -b s01-assignment`
4. Edit this `README.md` file (the one in your `AIE8/01_Prototyping Best Practices & Vibe Check` folder)
5. Perform a "Vibe check" evaluation your AI-Engineering-Challenge system using the five questions provided above 
6. For each Activity question:
    - Define the “Aspect Tested”
    - Comment on how your system performed on it. 
7. Provide an answer to `❓Question #1:` after the `✅ Answer:` prompt
8. Add, commit and push your modified `README.md` to your origin repository.

>(NOTE: You should not merge the new document into origin's main branch. This will spare you from update challenges for each future session.)

When submitting your homework, provide the GitHub URL to the tracking branch (for example: `s01-assignment`) you created on your AIE8 repo.

### The Advanced Build:
1. Follow all of the steps (Steps 1 - 8) of the Main Assignment above
2. Document what you changed and the results you saw in the `Adjustments Made:` and `Results:` sections of the Advanced Build's Assignment #1
3. Add, commit and push your additional modifications to this `README.md` file to your origin repository.

When submitting your homework, provide the following on the form:
+ The GitHub URL to the tracking branch (for example: `s01-assignment`) you created on your AIE8 repo.
+ The public Vercel URL to your updated Challenge project on your AIE8 repo.
