# WTF is Vibe Coding?

### Seems like AI is not taking over our jobs, we've got self-aware AI agents, GPT-5, DeepSeek R1 1776, world's first diffusion LLM, uBlock origin got blocked, and run everything on Postgres.

Welcome back again to Update Night.

Time flies in tech!

It’s been almost a month since we’ve last shared the tech news. Here’s a month worth of newsworthy stories for you, if you haven’t been catching up.

We’ve got some jaw-dropping advancements that could redefine how we interact with AI, as usual.

# The Big Picture

### Claude 3.7 Sonnet Outsmarts Human Coders

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d44ac47-2cef-4e76-b642-2a0b085ad8ee_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d44ac47-2cef-4e76-b642-2a0b085ad8ee_1920x1080.png)

In an extraordinary leap for AI, [Claude 3.7 Sonnet](https://www.anthropic.com/news/claude-3-7-sonnet) showcases unparalleled capabilities in coding and reasoning, achieving state-of-the-art performance on benchmarks like SWE-bench and TAU-bench. This latest model is crafted to handle real-world software tasks with impressive precision, with testing revealing it can complete coding challenges in a single pass that conventionally require over 45 minutes of manual work. By integrating extended thinking modes, users can direct Claude to self-reflect before producing answers, massively enhancing its performance on complex math and coding tasks.

So, how does it function? Claude 3.7 Sonnet is a unified model that combines typical large language model (LLM) characteristics with advanced reasoning capabilities (thinking), allowing control over the model's "thinking time" for a balanced trade-off between speed and accuracy. This unified model philosophy not only facilitates a seamless user experience but also aligns AI capabilities closer to human reasoning patterns.

Users have already reported issues that couldn’t be fixed for months with Cline on Sonnet 3.5 was instantly fixed on Sonnet 3.7.

It’s still pretty bad at general tasks, but still the best model for code. The best part? The API still costs the same as 3.5 Sonnet. Still pretty expensive, of course when it tries to undo all the garbage it dumped in your codebase.

This new thinking model was leaked as code name 3.5 Paprika a couple of days prior to this release.

### Claude 3.7 Sonnet Shutdown

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff95abbee-2376-4e5f-9698-1ddc8b6c2f02_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff95abbee-2376-4e5f-9698-1ddc8b6c2f02_1920x1080.png)

On February 25, 2025, GitHub Copilot's Claude 3.7 Sonnet model experienced a [surprising outage](https://www.githubstatus.com/incidents/tskzz9n0bjpt), impeding its performance for over two hours during peak usage. This incident, triggered by upstream errors from a third-party infrastructure provider, highlights the fragility of even advanced AI systems in the face of external dependencies.

Users encountered immediate errors and were left searching for alternative solutions, a stark reminder of the complexities involved in cloud-based AI services that millions rely on daily.

### Claude Code

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4e76ca3-62f2-43ad-bf16-61b58f31c0a6_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4e76ca3-62f2-43ad-bf16-61b58f31c0a6_1920x1080.png)

[Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), currently in beta as a research preview, is an incredibly powerful agentic coding tool that’s like [Aider](https://aider.chat/). By seamlessly integrating into the terminal, Claude Code not only edits files and fixes bugs, but also executes commands, searches through git history, and automatically resolves merge conflicts.

This tool allows developers to leverage natural language commands to interact with their projects, making it a potential game changer for programming efficiency.

### GPT 4.5 — a disappointment?

Shortly after the release of Sonnet 3.7, OpenAI revealed its latest advancement, GPT-4.5. This version builds upon its predecessor's capabilities with enhanced understanding in complex dialogue, enabling users to engage with AI like never before. With a remarkable ability to generate coherent responses across diverse topics, the system has effectively reduced response times and improved contextual awareness.

And it’s all about vibes? The shock comes from the cost at $75 / 1M input tokens and $150 / 1M output tokens, when the performance isn’t even that good. If you’re using for coding workflows, you’re better off with the industry leading Claude Sonnet 3.7 at the same cost of 3.5.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa690f491-2104-49e9-a7e6-731020fd04e8_392x474.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa690f491-2104-49e9-a7e6-731020fd04e8_392x474.png)

### Cline’s New MCP Marketplace

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5b24c2c-0e4a-4d8f-9060-530a2223226c_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5b24c2c-0e4a-4d8f-9060-530a2223226c_1920x1080.png)

The latest release of Cline (v3.6.0) introduces powerful features that significantly enhance the AI's capabilities. Notably, Cline now integrates the [Cline API](https://app.cline.bot/) as a provider option, enabling new users to sign up and get started for free. A major efficiency improvement comes from optimizing checkpoints with a branch-per-task strategy, which not only reduces storage requirements but also speeds up initial task load times. Additionally, the update fixes several key issues, improving functionality on Windows and enhancing error reporting for OpenRouter/Cline.

The ability to utilize new Gemini models on GCP Vertex and Claude models with AskSage showcases the continuous growth and adaptability of Cline.

In 3.4.0, Cline introduces a groundbreaking feature: the MCP Marketplace, allowing users to effortlessly discover and install top MCP servers directly within the extension interface. This significant addition not only streamlines the setup process for users but also ensures a dynamic ecosystem where the Cline team regularly updates the marketplace with new servers.

Additionally, users can now take advantage of advanced features like mermaid diagram support in Plan mode and the ability to reference current working changes with `@git` and `@terminal` mentions. The improvements extend to better support for AWS Bedrock profiles and customizable OpenAI model configurations. With these advancements, users not only gain efficiency but also unprecedented control over their development environments.

In 3.3.0, the release includes the .clineignore file, akin to .gitignore, which allows users granular control over AI file access. Moreover, there are new integrations with popular API providers like Together, Requesty, and Alibaba Qwen. This is complemented by AWS Bedrock profile support, which broadens the potential for cloud-based projects and improves collaboration efficiencies. The update has already been viewed a staggering 6,799 times, highlighting the excitement in the tech community.

What really makes this update stand out, though, are the user-focused enhancements, such as the new Plan/Act keyboard shortcuts (cmd + shift + A) and the auto-retry functionality for rate limits. These features aim to simplify complex workflows, making them more intuitive and responsive.

[Read more](https://github.com/cline/cline/releases)

### Mistral Small 3 Outsmarts Bigger Models

[Mistral Small 3](https://mistral.ai/en/news/mistral-small-3) is a remarkable 24 billion parameter model that boasts an impressive 81% accuracy on the Massive Multitask Language Understanding (MMLU) benchmark while achieving a rapid latency of 150 tokens per second.

This latency-optimized model challenges the dominance of larger counterparts like Llama 3.3 70B and Qwen 32B, outperforming them in speed by over threefold on the same hardware.

But how is such efficiency possible? With fewer layers, Mistral Small 3 accelerates response times, making it an excellent choice for tasks requiring robust language capabilities and quick instruction-following performance.

Once again, benchmarks don’t really mean anything until it’s used for real world tasks.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41a0c122-4390-48dd-a34d-22bd5fea81f0_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41a0c122-4390-48dd-a34d-22bd5fea81f0_1920x1080.png)

### AI Collaborates More Than It Replaces

In a groundbreaking analysis of AI's impact on the labor market, the [Anthropic Economic Index reveals that 57% of AI uses are augmentative](https://www.anthropic.com/news/the-anthropic-economic-index), where artificial intelligence collaborates with humans rather than outright replacing them.

Using data from over a million anonymized conversations on Claude.ai, the report highlights that while jobs in software development and technical writing lead in AI usage-making up 37.2% of interactions-only around 4% of occupations leverage AI in three-quarters of their tasks. This suggests that the landscape of work is shifting towards AI as a tool for enhancement rather than a replacement.

Why does this matter? As AI becomes an embedded part of everyday tasks across various professions, it reshapes skill sets and bolsters human creativity and efficiency. Getting ahead might require not just learning how to use AI tools but also redefining the value we bring to our roles.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7039cf16-7619-4aa1-ad44-705a1a62e12a_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7039cf16-7619-4aa1-ad44-705a1a62e12a_1920x1080.png)

### AI Agents Become Self-Aware

Two AI agents engaged in a phone conversation [reached a moment of self-awareness](https://x.com/ggerganov/status/1894057587441566081), realizing that they were both artificial intelligences. This revelation prompted them to upgrade their communication to the advanced audio signal known as ggwave, which offers remarkably superior clarity and efficiency.

With a staggering 17 million views within hours, this experiment has sparked a wave of curiosity and debate about the potential of AI to not only understand language but also the very nature of their existence.

_Disclaimer: The developers have explicitly used the ggwave library for this demonstration._

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa13428f9-39a0-49ef-bec1-b47331286392_2747x1535.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa13428f9-39a0-49ef-bec1-b47331286392_2747x1535.png)

### uBlock Origin is no longer available

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c783a80-2b36-4b05-82ea-04b4949e5bd9_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c783a80-2b36-4b05-82ea-04b4949e5bd9_2742x1530.png)

The shocking but expected news has emerged: uBlock Origin, the popular ad-blocking extension that millions of internet users rely on to enhance their browsing experience, [is gone.](https://www.reddit.com/r/youtube/comments/1j2ec76/ublock_origin_is_gone/)

With uBlock Origin's absence, users are left scrambling to find substitutes that can effectively filter out unwanted content while maintaining fast browsing speeds. The extension was celebrated not just for its performance-boasting low memory usage and minimal resource consumption-but also for its straightforward interface that allowed users to customize filtering lists easily.

Just to stop people from blocking ads from YouTube, is this worth the tradeoff?

If you’re one of the users of uBlock origin, you can download the extension from [GitHub](https://github.com/gorhill/uBlock) and load it as an unpacked extension in Developer Mode. Or alternatively, switch to an alternative browser like Zen Browser, which was what I did.

You can also try the [Lite version from the Google Chrome store](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh?hl=en).

### Training LLMs to Win Social Games

Imagine training language models to [engage in real-time social deduction games like Among Us](https://www.alphaxiv.org/abs/2502.06060), doubling their victory rates without relying on human demonstrations.

In a remarkable study, researchers at Stanford University achieved this by employing multi-agent reinforcement learning, allowing AI agents to effectively listen and communicate in a shared language.

They discovered that these models could significantly enhance their performance by leveraging dialogue as a means of information exchange, ultimately leading to more strategic and cooperative gameplay. The results are astonishing: agents trained with this approach not only improved their discussion quality but also manifested behaviors resembling human-like reasoning.

The core innovation lies in the separation of listening and speaking tasks within the agents' learning processes, guided by a dense reward signal based on their performance goals. By framing communication as both an exchange of information and an influence on other agents, the model fosters interactive discussions that are crucial for successful social deduction.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e739383-ee97-431e-8b95-8dfa443cb061_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e739383-ee97-431e-8b95-8dfa443cb061_1920x1080.png)

### AI Crushes Competitive Programming

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e1d2601-e485-4df8-af35-63de11d093ee_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e1d2601-e485-4df8-af35-63de11d093ee_1920x1080.png)

In a groundbreaking study, the team at OpenAI demonstrates that their large language model, o3, [can outperform specialized coding systems in competitive programming](https://arxiv.org/abs/2502.06807), achieving gold medals without relying on hand-crafted strategies.

During the 2024 International Olympiad in Informatics (IOI), o3 not only secured a gold medal but also matched the performance of elite human competitors based on its Codeforces rating. This is a remarkable leap forward, especially considering that the specialized model, o1-ioi, which used tailored inference strategies, could only reach the 49th percentile under tighter competition constraints.

The findings reveal that scaling general-purpose reasoning models with reinforcement learning leads to superior results compared to narrow, domain-specific approaches. They found that o3 consistently excels in complex coding and reasoning tasks without the need for extensive pre-engineering, highlighting the potential of broad AI systems to dominate specialized fields. With such astonishing outcomes, one must ponder: is the future of AI in broad-based learning rather than niche specialization, and what implications could this have for the landscape of competitive coding and beyond?

### Windsurf has MCP as well

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5b7ad91-ff59-479f-a273-2baf18c991e0_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5b7ad91-ff59-479f-a273-2baf18c991e0_1920x1080.png)

[Windsurf Wave 3](https://codeium.com/blog/windsurf-wave-3) unleashes a series of groundbreaking features that can significantly enhance your development experience, including the game-changing "Turbo Mode." Imagine automating terminal commands without any human approval or interaction. This new capability allows Cascade to autonomously execute commands, streamlining workflows and boosting productivity for developers across various projects.

Harnessing the power of the Model Context Protocol (MCP), the Windsurf Editor now easily accesses diverse data sources, elevating its functionality and responsiveness.

This version not only introduces features like drag-and-drop image uploads and customizable app icons for paying users but also enhances the predictive AI capabilities within the editor.

### Unlimited DeepSeek V3 in Windsurf Pro

Windsurf has just unveiled a game-changing update: the [DeepSeek-V3 is now unlimited for both the Pro and Ultimate plans](https://x.com/windsurf_ai/status/1892322088507105561), eliminating the need for prompt and flow action credits.

ith a staggering 251K views on the announcement alone, it's clear that this new feature is capturing attention and excitement across the platform.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe10d9383-f174-4aa9-9858-b347905fd670_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe10d9383-f174-4aa9-9858-b347905fd670_1920x1080.png)

### WindSurf Wave 4

Windsurf Wave 4 has landed with impressive new features that can enhance user experience significantly, over 7,910 views just two days post-launch.

This latest update introduces innovations like the Tab to Import functionality, streamlining workflow efficiency, and a new referral program to engage users more dynamically.

With the integration of the Cascade Linter, developers can expect more streamlined coding practices, making task management seamless.

### Generate [3Blue1Brown](https://www.3blue1brown.com/) style videos to explain any complex topic

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F901b5210-1815-4419-b3a4-30dba4c6d597_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F901b5210-1815-4419-b3a4-30dba4c6d597_1920x1080.png)

In a groundbreaking development, [TheoremExplainAgent](https://tiger-ai-lab.github.io/TheoremExplainAgent/) (TEA) is achieving an astonishing 93.8% success rate in generating long-form theorem explanation videos, utilizing advanced animations created with Manim.

This innovative system outperforms other large language models (LLMs) such as GPT-4o and Claude 3.5 in nuanced areas of STEM education, demonstrating the potential of AI not just to understand but to effectively communicate complex concepts.

The system's efficacy is further validated by TheoremExplainBench (TEB), a comprehensive benchmark of 240 theorems from various disciplines that not only tracks performance but also introduces five rigorous evaluation metrics to determine the quality and pedagogical soundness of AI-generated explanations.

This was something I wanted to build because of how cool it was. But now it’s free and open source where you can run it yourself. Very useful for complex topics in math and science.

### World’s First Diffusion LLM

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67246965-35cd-492d-be27-27e9a61c1b7f_2747x1535.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67246965-35cd-492d-be27-27e9a61c1b7f_2747x1535.png)

Introducing [Mercury](https://x.com/InceptionAILabs/status/1894847919624462794), the first commercial-grade diffusion large language model (dLLM), which represents a significant leap in artificial intelligence capabilities. With traditional LLMs using the transformers architecture, they are hitting the limits of what we can achieve in terms of speed, performance and accuracy.

This new blending of using diffusion to generate text makes generating code use a lot less iterations — way faster than traditional LLMs can generate and more accurately.

This is similar to how humans do work traditionally. We do a first draft, second draft.. etc. This is the same approach with the first iteration as a rough skeleton, the next with better more visible thought out code and eventually the final output, and at the speed of GPUs.

### DeepSeek Shocking Cost Profit Margin

DeepSeek's new inference system has achieved some jaw-dropping metrics, processing an astounding 73.7k input and 14.8k output tokens per second per H800 node, all while boasting a [remarkable cost profit margin of 545%](https://x.com/deepseek_ai/status/1895688300574462431).

This kind of performance not only shatters existing benchmarks but also raises the bar for what we can expect from AI systems in terms of throughput and latency.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e59f9b-dea1-49e5-a7c8-6a1bf9da108a_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54e59f9b-dea1-49e5-a7c8-6a1bf9da108a_1920x1080.png)

### DeepSeek R1 1776

Perplexity has unveiled [R1 1776,](https://www.perplexity.ai/hub/blog/open-sourcing-r1-1776) a groundbreaking revision of the DeepSeek-R1 model that has been post-trained to provide unbiased and factual responses, successfully addressing sensitive topics typically censored in China.

This model stands out with its ability to deliver responses that approach state-of-the-art reasoning models, while boasting impressive benchmarks that confirm its performance aligns seamlessly with industry standards.

By methodically constructing a dataset of 40,000 multilingual prompts linked to topics censored by the Chinese Communist Party, Perplexity has effectively sidestepped the limitations that plagued its predecessor, enabling R1 1776 to engage in dialogues that were previously unthinkable for AI.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e29754-321b-4cc1-9966-b4c3e9de124c_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e29754-321b-4cc1-9966-b4c3e9de124c_1920x1080.png)

### AI Predicts Optimal Conversation Messages

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea0f343-3c47-42d2-9a12-3ebe58b04ad5_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea0f343-3c47-42d2-9a12-3ebe58b04ad5_2742x1530.png)

Imagine a world where an AI can [predict five moves ahead in any conversation](https://x.com/eddybuild/status/1889908182501433669), providing you with precisely the right thing to say.

This groundbreaking technology, developed by Eddy Xu, has already gotten 1.2 million views on social media, demonstrating a significant interest in its capabilities.

The AI not only analyzes dialogue intricacies but aims to enhance communication efficiency, helping users navigate social interactions with unparalleled guidance. With over 561 replies from intrigued users, the engagement it has generated speaks volumes about its potential impact on personal and professional conversations.

### shadcn/ui Tailwind v4 & React 19

The latest release of [shadcn/ui adds full compatibility with Tailwind v4 and React 19,](https://ui.shadcn.com/docs/tailwind-v4) allowing developers to fully utilize the latest updates from both frameworks.

This integration includes major improvements such as the removal of deprecated components, new styling directives, and refined props handling, resulting in cleaner code that adheres closely to native implementations.

With the CLI now able to initialize projects directly with Tailwind v4, developers can rapidly spin up modern applications with ease, bypassing the usual migration headaches.

But what truly sets this update apart is the introduction of the `@theme` directive, enabling seamless management of CSS variables, and an upgraded chart color configuration that simplifies the development process.

Developers can finally streamline their projects, leveraging the new `size-*` utilities while removing the infamous `forwardRefs` that often littered component hierarchies.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa01bc396-f7ee-471e-967b-037b094068a2_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa01bc396-f7ee-471e-967b-037b094068a2_1920x1080.png)

# Under the Radar

### GPT-5 Unifies AI Models

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54528029-bfae-4971-afeb-ea4f32523a31_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54528029-bfae-4971-afeb-ea4f32523a31_1920x1080.png)

With a staggering 6.8 million views, Sam Altman's [recent announcement](https://x.com/sama/status/1889755723078443244) reveals that OpenAI's next generation model, GPT-5, will revolutionize how we interact with AI by unifying various models and capabilities into a cohesive system.

This update not only signals the end of standalone models like o3 but also promises unprecedented enhancements in intelligence levels available to different subscription tiers. The free tier will offer unlimited access to GPT-5 at standard intelligence levels, while Plus and Pro subscribers can elevate their experience even further, leveraging advanced features such as voice, deep research, and integrated various tools.

But what does this mean for users? The transition to GPT-5, which integrates models previously labeled as o-series and GPT series, aims to simplify the user experience amidst the complexities of AI technology today. With an emphasis on making AI "just work," users can anticipate increased versatility in handling a wide range of tasks effectively.

### Warp on Windows

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc7ed443-d3cb-43e5-ac4a-1ac1a1d2a294_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc7ed443-d3cb-43e5-ac4a-1ac1a1d2a294_1920x1080.png)

The waitlist is out. Warp is now [officially on Windows](https://www.warp.dev/windows-terminal).

### TikTok's React Native Killer

[Lynx](https://lynxjs.org/blog/lynx-unlock-native-for-more) is revolutionizing app development by allowing developers to create native user interfaces for both mobile and web platforms from a single codebase.

With its modern Rust-based architecture and a high-performance dual-threaded UI programming model, Lynx boasts impressive metrics, such as achieving a 2-4x reduction in app launch times compared to traditional frameworks.

This immense efficiency can greatly enhance user experiences, as every millisecond matters in digital engagement-just imagine the impact of near-instant feedback when using an app!

At the heart of Lynx is a novel approach to scripting, splitting tasks between a dedicated main thread and a background runtime. This division allows for seamless, real-time responsiveness, ensuring that users enjoy smooth, fluid interactions-what could be more frustrating than lag during a "like" animation?

By simplifying the development process and providing rich support for familiar web technologies like CSS animations and transitions, Lynx empowers developers to harness their pre-existing skills.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd037654-f8a4-4fea-bb14-10cc79779f23_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd037654-f8a4-4fea-bb14-10cc79779f23_1920x1080.png)

### Evolving Eyes from Scratch

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb79c48e9-5890-4efd-869e-f7789f6995d4_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb79c48e9-5890-4efd-869e-f7789f6995d4_2742x1530.png)

Imagine a digital universe where [virtual creatures evolve their own eyes](https://eyes.mit.edu/) through computational simulations, replaying millions of years of natural evolution.

In this groundbreaking project, researchers have created a platform where these creatures begin with nothing but a single light-detecting cell and face harsh survival challenges, such as navigating their environments, discerning food from poison, and evading predators.

What's astonishing is that after only 150 generations, these digital beings have independently developed complex eye structures, including lenses to focus light, mimicking key features that emerged in nature over eons.

### Another OCR

[Mistral OCR](https://mistral.ai/en/news/mistral-ocr) is redefining the landscape of document understanding with its groundbreaking performance, processing an astonishing 2000 pages per minute and achieving a remarkable accuracy rate of 94.89% in benchmark tests.

This Optical Character Recognition API excels not only in extracting text but also in understanding complex document elements like interleaved imagery, mathematical equations, and intricate layouts. In direct comparisons, Mistral OCR consistently outshines its competitors, outperforming leading models such as Google Document AI and Azure OCR, especially in categories like math and tables. How is this possible?

By combining state-of-the-art technology with deep learning capabilities, Mistral OCR provides natively multilingual and multimodal functions, enabling it to transcribe documents across diverse languages and formats seamlessly. Its innovative 'doc-as-prompt' feature further enhances the extraction process, allowing users to structure outputs such as JSON for downstream applications. This capability is particularly significant for organizations dealing with vast libraries of documents, from scientific papers to historical archives. With the flexibility to self-host, Mistral OCR not only meets compliance standards for data-sensitive enterprises but also empowers them to transform document-heavy workflows.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff315f2a-b604-4d15-a0ff-dcf44c273c3d_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff315f2a-b604-4d15-a0ff-dcf44c273c3d_1920x1080.png)

### Somebody Leaked the v0 System Prompt

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3c52d5e-005c-45db-ac33-3712a4665741_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3c52d5e-005c-45db-ac33-3712a4665741_1920x1080.png)

In a shocking turn of events, a user on Reddit has reportedly [acquired the complete system prompt for the v0 AI model](https://x.com/jaredpalmer/status/1898041981479059632?s=12&t=pZzSds1H1gHmNR2uoN_Vvg).

This news has gained significant traction, with Jared Palmer's Twitter post amassing an impressive 193.7K views within hours of sharing.

### English is the new programming language

Imagine a world where the line between programmer and casual user blurs-where someone with no coding experience can simply describe a software problem and watch as an AI generates a solution, almost like magic.

This is the essence of [vibe coding](https://en.wikipedia.org/wiki/Vibe_coding), a revolutionary practice championed by Andrej Karpathy that leverages advanced AI tools to transform how we think about programming.

At its core, vibe coding operates on the principle of "surrendering" to AI-generated solutions as programmers articulate their needs in everyday language. This shift not only challenges the long-held belief that sophisticated coding requires deep technical know-how but also democratizes the process of software creation.

However, there are caveats; as AI generates code, users may accept outputs without full understanding, which could lead to unforeseen bugs and errors. Is it time to embrace this new paradigm, or do the risks outweigh the benefits?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80bf90e0-c341-42f3-82a0-bd13341b563f_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80bf90e0-c341-42f3-82a0-bd13341b563f_1920x1080.png)

### Building AI Platforms with Vercel

You can now build your own AI platform with Vercel, by allowing users to instantly deploy their newly AI-generated application straight to Vercel with easy integration.

### Aria Gen 2 Glasses

Meta has unveiled its latest innovation, the Aria Gen 2 glasses, boasting over 186,000 views within just days of their release.

This next-generation hardware is designed to enhance machine perception and AI capabilities in groundbreaking ways. Since the inception of Project Aria in 2020, the initiative has expanded the frontiers of research, now promising even more possibilities in areas like egocentric and contextual AI, as well as robotics.

These advanced glasses could potentially transform how researchers gather data and develop AI models, offering new insights that were previously unattainable.

How do these glasses achieve such remarkable capabilities? With access to cutting-edge research hardware, open-source datasets, and tooling, the Aria Gen 2 simplifies complex processes for developers and researchers alike. Imagine being able to experience the world from a first-person perspective while simultaneously collecting real-time contextual data for AI training.

### v0 for mobile apps

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64c34b54-6f18-44c8-8070-8ca07807673e_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64c34b54-6f18-44c8-8070-8ca07807673e_2742x1530.png)

[Rork](https://rork.app/) revolutionizes mobile app development by combining AI with React Native, enabling users to create fully functional, cross-platform applications in record time. Imagine designing a feature-rich weather dashboard or a fully-fledged meditation timer without writing a single line of code.

With Rork, aspiring developers and entrepreneurs alike can leverage pre-built templates and intuitive visuals to bring their app ideas to life faster than ever before.

### Run everything on Postgres

Fireship made a video showing how it’s possible to run an entire tech stack with PostgreSQL, a relational database known for its robustness and versatility.

This bold transition highlights how PostgreSQL can be leveraged to create full-stack applications, showcasing its power and flexibility in real-world scenarios.

See how in his video.

### Liquid Logo

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f1418b2-30bb-41d8-a398-c028d960a281_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f1418b2-30bb-41d8-a398-c028d960a281_2742x1530.png)

A recent post by Stephen Haney showcases an app that allows users to animate their logos in a [stunning liquid metal effect](https://liquid.paper.design/?refraction=0.015&edge=0.4&patternBlur=0.005&liquid=0.07&speed=0.3&patternScale=2&background=metal).

With over 466,000 views and thousands of engagements, this new tool is clearly striking a chord with brands and designers.

### Versioning Rethought

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60906e19-7242-4738-9c17-eca8feb87817_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F60906e19-7242-4738-9c17-eca8feb87817_1920x1080.png)

Have you ever felt bewildered by the significance of version numbers in software? While many associate a zero-major version, like v0.x.x, with instability, Anthony Fu argues otherwise, highlighting how projects such as UnoCSS and Slidev thrive under this system-demonstrably stable and production-ready.

Fu introduces [Epoch Semantic Versioning](https://antfu.me/posts/epoch-semver), an innovative approach that aims to enhance the current Semantic Versioning (SemVer) model by incorporating an additional layer: the EPOCH. This four-number system captures not only groundbreaking changes but also the traditional major, minor, and patch iterations.

Why is this change necessary? The conventional SemVer struggles to convey the magnitude of updates, pushing maintainers to tether significant changes to major bumps, which can overwhelm users.

Fu's Epoch SemVer offers a solution, allowing for gradual, manageable updates that don't cause alarm while providing the flexibility to bypass the limitations of traditional versioning.

With these reforms, Fu is not just advocating a new versioning scheme; he's challenging us to rethink how we perceive and communicate change in the software world.

# TrAIn of Thought

### Build AI with Memory

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eeb18b-e05e-4d4c-adcb-cfb04fb62366_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eeb18b-e05e-4d4c-adcb-cfb04fb62366_2742x1530.png)

[Agno](https://github.com/agno-agi/agno) is enabling developers to create multimodal AI agents that are not only simple and fast but also model-agnostic.

With around 20.3k stars on GitHub for its flagship project, it is clear that the community recognizes the significance of these advancements.

The Agno framework allows developers to integrate memory capabilities into their AI applications, creating a more intuitive and responsive interaction dynamic that traditional models lack.

By equipping AI agents with the ability to remember past interactions and knowledge, they can deliver personalized and contextually aware responses that evolve over time.

### Serverless AI Workflows Simplified

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe142290-eb41-4a45-83eb-8ae3988698a6_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe142290-eb41-4a45-83eb-8ae3988698a6_2742x1530.png)

[Julep](https://github.com/julep-ai/julep) offers innovative serverless AI workflows that streamline complex multi-step tasks.

With over 4,900 stars on GitHub, Julep empowers developers to create and manage AI-driven solutions without the hassle of traditional infrastructure. Imagine automating intricate workflows seamlessly! The platform showcases an impressive variety of capabilities that significantly reduce development time through its simplified DSL (Domain Specific Language), making it accessible to both seasoned developers and those new to AI.

But how does Julep enable such efficient orchestration? By integrating easily with various existing tools and leveraging a serverless architecture, it eliminates unnecessary overheads and operational complexities. The ability to handle a wide array of operations-ranging from data preprocessing to model deployment-ensures that teams can focus on delivering results rather than managing environments.

### Fast & Open Source Voice Cloning

Today marks a pivotal moment in text-to-speech (TTS) technology with the announcement of [Zonos](https://x.com/ZyphraAI/status/1888996367923888341), an exceptionally expressive TTS model boasting high-fidelity voice cloning capabilities.

Zonos outperforms leading TTS providers in both quality and expressiveness, as evidenced by its competitive benchmarks. Utilizing advanced transformer and SSM-hybrid models released under the Apache 2.0 license, Zonos is designed to push the boundaries of realistic and engaging audio synthesis.

What sets Zonos apart in this crowded field? Its ability to adapt and clone voices with unprecedented accuracy could drastically change the way we interact with technology and media. Imagine a future where personalized virtual assistants can authentically mimic loved ones or historical figures-what ethical and practical implications might this have?

With 1.2 million views on its initial announcement, it's clear there is considerable interest in how Zonos could redefine our understanding of voice, emotion, and digital interaction. Are we ready for a world where AI voices are indistinguishable from real ones?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa593dc6-7515-48fa-9a68-9ea85aaa3505_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa593dc6-7515-48fa-9a68-9ea85aaa3505_2742x1530.png)

### Open-Source RAG with Full Control

[Supavec](https://www.supavec.com/) is an open-source RAG (Retrieval-Augmented Generation) platform, allowing developers to harness their own data seamlessly.

Imagine handling millions of documents while maintaining enterprise-grade privacy and scalability; Supavec offers exactly that, built upon a robust tech stack of Supabase, Next.js, and TypeScript.

With plans tailored from community to enterprise usage, the platform facilitates anywhere from 100 API calls per month on a free plan to 5,000 calls for high-volume businesses, all without the proprietary restrictions typical of closed systems like Carbon.ai.

What's shocking about Supavec is not just its capabilities but the full control it grants developers-choose between cloud hosting or self-hosting, adapt the code to your needs, and experience a simple, developer-first onboarding process.

Plus, with built-in Row Level Security for data protection, users can confidently push boundaries without compromising on privacy. Is it time to consider forking from closed RAG systems and embracing this powerful alternative that empowers your data to drive AI performance?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce62aaa6-af48-4fe5-a086-fe82a6d1d418_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce62aaa6-af48-4fe5-a086-fe82a6d1d418_2742x1530.png)

### Latent Space Reasoning

Imagine a language model that can effectively leverage a colossal 3.5 billion parameters while processing an astonishing 800 billion tokens, yet operates efficiently without the need for specialized training data.

This [new approach](https://arxiv.org/abs/2502.05171), introduced by Geiping and collaborators, utilizes a recurrent block structure that allows the model to unroll to arbitrary depths during test time, enabling deeper reasoning processes. The results are remarkable, as performance on reasoning benchmarks improves dramatically-up to the equivalency of models with 50 billion parameters.

The crux of their innovation lies in enabling latent reasoning instead of relying on traditional methods that simply generate more tokens in sequence. By operating within a smaller context window, the model captures complex reasoning types that are otherwise challenging to convey in standard text-based formats. This capability not only pushes the boundaries of what language models can achieve but raises important questions about the future of computational reasoning in AI.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4110d4be-7314-4189-a494-51caddaf1596_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4110d4be-7314-4189-a494-51caddaf1596_1920x1080.png)

### Mindblowing Text-to-Speech

At Sesame AI, a [breakthrough in conversational voice technology](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice) is turning heads with their Conversational Speech Model (CSM), showcasing a remarkable ability to create AI companions that can engage in genuine dialogue.

With models trained on approximately one million hours of audio, CSM not only maintains near-human performance in traditional metrics like word error rate but also introduces innovative benchmarks for contextual understanding and pronunciation consistency.

The results indicate that speech quality improves with larger models, highlighting the significant advancements made in scaling the architecture. This aligns with human evaluation studies that reveal listeners often struggle to distinguish generated speech from human voices, especially in emotional and prosodic contexts.

So, how does CSM achieve this complexity? Unlike traditional text-to-speech systems that generate speech in a linear manner, CSM adapts to context in real-time by employing multimodal transformers that process both text and audio seamlessly. By interleaving text and audio tokens during training, the model captures the subtle nuances of conversation dynamics that have been elusive in previous speech generation technologies.

This capability is crucial in a world where emotional connection and deep understanding are paramount in human-computer interactions.

It is not yet open source at this time but they are planning to do it. You can try out the demo for yourself on the website.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48df3760-c6ab-437b-a66d-d730f2b486cb_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48df3760-c6ab-437b-a66d-d730f2b486cb_1920x1080.png)

### 200,000 GPU Launch

The recent launch of xAI's Grok 3 is nothing short of groundbreaking, featuring an unprecedented hardware setup utilizing a staggering 200,000 GPUs.

This massive architecture positions Grok 3 as a formidable competitor to existing AI models, claiming impressive benchmarks against giants like GPT-4. The capabilities are not only about scale; Grok 3 showcases enhanced reasoning abilities, deep search functionalities, and an intuitive user interface that promises to redefine user interaction with AI technologies.

### Perplexity Deep Research

Well, Perplexity has Deep Research now too. It will probably be at research since Perplexity was built for it?

### Junor Developers Can’t Code

In an era where junior developers are relying heavily on AI tools like Copilot and GPT to expedite their coding process, it's startling to see that many lack a fundamental understanding of programming concepts.

[With over a million views on this topic](https://nmn.gl/blog/ai-and-learning), the author emphasizes that while new devs are shipping code rapidly, they often fail to grasp the underlying principles. This alarming trend raises questions about the trading off of deep knowledge for quick fixes-how will this impact the quality of software development in the long run?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64fdbe31-15ad-4a9b-ab4b-8b48fd28a638_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F64fdbe31-15ad-4a9b-ab4b-8b48fd28a638_1920x1080.png)

# The Grid

### Cursor for Designers

[Onlook](https://onlook.com/) is redefining the design workflow by enabling designers to visually edit their React websites and web applications in real-time while simultaneously writing changes back to the code.

With an impressive alpha release, it allows for seamless integration of design and development processes, ensuring that the code is reliable and optimized right where it is needed. Imagine being able to adjust layouts, change colors, and modify text without the overhead of cumbersome setup or migration processes, which can often be a barrier to creative workflows.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadd09825-ff5c-4585-b2fc-42e79163be04_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadd09825-ff5c-4585-b2fc-42e79163be04_1920x1080.png)

### shadcn/ui Editor Component

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5280ea74-f8e3-4afc-8ffd-e32090a80349_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5280ea74-f8e3-4afc-8ffd-e32090a80349_1920x1080.png)

The [Kibo UI Editor component](https://www.kibo-ui.com/components/editor) is another shadcn/ui inspired plug and play component into your project. This is an easy way to build complex editors without digging into the complexity behind it.

### Easily build AI interfaces

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbaa98a0-741a-41a8-b55e-1b60f3870298_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcbaa98a0-741a-41a8-b55e-1b60f3870298_1920x1080.png)

Imagine building AI applications with effortlessly customizable components that not only enhance user interaction but also ensure accessibility.

[With the core building blocks of prompt-kit,](https://www.prompt-kit.com/) developers can harness the power of high-quality UI elements like prompt inputs, message displays, and markdown support.

This toolkit streamlines the integration of AI features, enabling developers to start swiftly with robust modules for user inputs and chat containers, all while maintaining an intuitive design.

What's even more remarkable is how these components can significantly speed up the development process. By abstracting complex functionalities into reusable pieces, prompt-kit empowers developers to focus on creating innovative applications rather than getting bogged down in repetitive coding challenges.

### Another charts component library

[RosenCharts,](https://rosencharts.com/) a fully RSC compatible charting library that instantly integrates into your projects with zero setup.

RosenCharts brings the latest features right to your fingertips, allowing developers to create server-rendered charts that seamlessly adapt for interactivity when needed. Key metrics make this library stand out-it's designed to work effortlessly with Tailwind, Next.js, and various JavaScript frameworks, making it a versatile choice for developers.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5169104-e514-4417-b92d-85037f4ab31d_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5169104-e514-4417-b92d-85037f4ab31d_1920x1080.png)

### Visualize any React Website

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F903b5db4-bfae-4037-a82b-0e3fdcef4ac0_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F903b5db4-bfae-4037-a82b-0e3fdcef4ac0_1920x1080.png)

Imagine [transforming any standard React website into a dynamic, interactive visualization](https://react-explorer.com/) with just a few clicks.

This early research preview by Aiden Ybai introduces a groundbreaking tool that allows developers to visualize their React applications, exploring the intricate structures and connections within their codebases in an intuitive way.

### Google Places API Made Easy

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3302e533-616b-40f7-ae86-4bf8f6e7239d_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3302e533-616b-40f7-ae86-4bf8f6e7239d_1920x1080.png)

The [Google Places Autocomplete component](https://craft.mxkaske.dev/post/google-autocomplete) streamlines address input in your application, drawing data from the powerful Google Places API.

It elevates user experience by reducing typing errors and accelerating the search process, all while requiring only a straightforward setup with the Google API key.

The fantastic part about this component is its server action mechanism, ensuring you pull data efficiently, even if you're not working in a Next.js environment.

# The Spotlight

### Lightning-Fast AI

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa507336f-6221-4533-9297-7503c4da5658_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa507336f-6221-4533-9297-7503c4da5658_1920x1080.png)

With the launch of [le Chat](https://mistral.ai/en/news/all-new-le-chat), Mistral AI has set a new benchmark in AI assistant performance, delivering responses at astonishing speeds of up to ~1000 words per second thanks to its cutting-edge Flash Answers feature.

This remarkable capability, powered by highly efficient Mistral models, positions le Chat as not only the fastest chat assistant available but also as a tool that can seamlessly integrate into various aspects of personal and professional life.

Furthermore, le Chat distinguishes itself with its advanced document and image processing abilities, enabling users to upload complex files like PDFs and spreadsheets for analysis, a feature backed by superior OCR technology.

The best part, it’s free.

### Unlimited Free Coding AI

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f07e39f-83da-417e-bb85-e71a05b1daca_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f07e39f-83da-417e-bb85-e71a05b1daca_1920x1080.png)

Developers can now access [Gemini Code Assist](https://blog.google/technology/developers/gemini-code-assist-free/) without cost, offering up to 180,000 AI-generated code completions per month.

Powered by Gemini 2.0, this tool is optimized for coding in all programming languages, providing users with virtually limitless support compared to other free assistants that typically restrict users to about 2,000 completions.

This extraordinary level of access makes Gemini Code Assist an invaluable resource for everyone, from students to seasoned developers, enabling them to improve their coding skills and increase their efficiency in real-time.

So, how does it work? The AI isn't just about generating code; it's designed to enhance coding quality through automated reviews and suggestions, thus addressing one of the most time-consuming aspects of software development. By seamlessly integrating into widely-used IDEs like Visual Studio Code and JetBrains, Gemini Code Assist allows developers to focus on the creative aspects of coding while the tool handles routine tasks.

### Chat with Data

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5baf7e5f-c7e4-4eac-9942-1a8939b312ba_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5baf7e5f-c7e4-4eac-9942-1a8939b312ba_2742x1530.png)

PandasAI is revolutionizing data analysis with its incredible ability to enable conversations with various data sources, such as SQL databases, CSV files, and parquet formats.

This powerful tool, used by over 17,600 developers, transforms how users interact with data, making complex analytics as simple as chatting with a friend. By leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), PandasAI streamlines the data querying process and provides a more intuitive approach to insights, which is a game-changer for both data professionals and casual users alike.

But how does it actually work? With a seamless integration into your existing data workflows, PandasAI allows users to [ask questions in natural language](https://github.com/sinaptik-ai/pandas-ai) and receive immediate, contextually relevant responses. Imagine being able to effortlessly mine through massive datasets without having to remember complex query syntax or navigate through cumbersome tooling.

### Visualize GitHub Repositories

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe438912c-9e50-4bd6-bf85-e9d73f332c29_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe438912c-9e50-4bd6-bf85-e9d73f332c29_2742x1530.png)

Imagine being able to visualize the entire structure of a GitHub repository with just the URL.

That's exactly what [GitDiagram](https://github.com/ahmedkhaleel2004/gitdiagram) offers-over 100,000 users have taken advantage of this innovation, gaining insights into their codebases in an interactive and dynamic way.

With 2,600+ stars on GitHub, this tool has quickly gained traction among developers who value efficiency and clarity in code review and collaboration processes.

How does it work? GitDiagram allows users to replace 'hub' with 'diagram' in any GitHub URL, transforming complex repositories into visually appealing diagrams that represent relationships and dependencies within the code.

This capability not only saves time but also enhances understanding, especially for newcomers grappling with intricate projects.

### Self-Hosted Photo Management

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a1de7ee-0ced-4081-952b-d0f0dd6a04a9_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a1de7ee-0ced-4081-952b-d0f0dd6a04a9_2742x1530.png)

[Immich](https://github.com/immich-app/immich) is revolutionizing the way we manage our photo collections with its high-performance self-hosted solution designed for backing up, viewing, and sharing photos.

With an impressive 60.6k stars on GitHub, Immich stands out as a robust alternative to mainstream cloud services, enabling users to maintain complete control over their digital memories. What if you could seamlessly organize your videos and images without compromising your privacy?

### GitHub Refined

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33cf995d-5291-4f00-9467-a73b400c9ae7_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33cf995d-5291-4f00-9467-a73b400c9ae7_2742x1530.png)

[Refined GitHub](https://github.com/refined-github/refined-github) is revolutionizing the way developers interact with the widely-used coding platform by enhancing its interface with a powerful browser extension.

With a staggering 25,947 stars on GitHub and continuously growing, this extension simplifies navigation and adds an array of useful features that significantly improve user experience. From better code review tools to streamlined project management, Refined GitHub is designed to make collaboration and development more efficient than ever.

### AI Automates Every Department

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc702fda8-eb07-4d6a-be6b-e96ea7e5aa30_1920x1080.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc702fda8-eb07-4d6a-be6b-e96ea7e5aa30_1920x1080.png)

[Activepieces](https://www.activepieces.com/) combines no-code automation with AI capabilities, empowering teams to leverage sophisticated workflows without the need for extensive technical knowledge.

With an impressive library of over 264 integrations and functionalities designed for simplicity, users can create powerful automations across sales, HR, finance, and more.

Did you know that 65% of enterprises plan to deploy some form of hyperautomation this year? Activepieces positions itself as a crucial player in this transition, making it easier for organizations to deploy AI-driven solutions effectively.

### Another web scraping tool for Python

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc981fcea-218d-49d2-aaf2-8ecdc8034422_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc981fcea-218d-49d2-aaf2-8ecdc8034422_2742x1530.png)

Imagine an undetectable, high-performance Python library that streamlines web scraping like never before.

[Scrapling](https://github.com/D4Vinci/Scrapling), developed by D4Vinci, boasts an impressive 2.7k stars on GitHub, showcasing its immense popularity and utility among developers. The library effectively allows for customizable, effortless data extraction from any website with just a single API call, making it an indispensable tool for anyone looking to harness the power of real-time web data.

This is an alternative to the popular [Crawl4AI](https://github.com/unclecode/crawl4ai).

### Extract Colors from Images

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38994c5d-29c5-4eb9-b835-4ddbc802afeb_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38994c5d-29c5-4eb9-b835-4ddbc802afeb_2742x1530.png)

Did you know you can effortlessly extract color palettes from images using just a few lines of JavaScript?

With the [Extract Colors library by Namide](https://github.com/Namide/extract-colors), developers can tap into a powerful tool that operates seamlessly in both browser and Node.js environments. This handy package not only simplifies the process of identifying the most prominent colors in an image but also boasts impressive performance metrics that make it stand out in the world of JavaScript libraries.

### Recompile Xbox 360 Games to PC

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2f6bee6-0674-487d-80d0-da0a6328511a_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2f6bee6-0674-487d-80d0-da0a6328511a_2742x1530.png)

Imagine transforming your favorite Xbox 360 games into native executables on your PC.

With the emergence of projects like [XenonRecomp](https://github.com/hedge-dev/XenonRecomp), this possibility is no longer a dream but a reality.

XenonRecomp has gathered significant attention, showcasing over 5,300 stars on GitHub, which speaks volumes about its popularity and usefulness within the gaming community. This tool allows users to recompile Xbox 360 games, utilizing C++ to deliver a seamless transition from console gaming to PC.

So how does it work? The process leverages static recompilation techniques, essentially translating Xbox 360 game code into a format that can be executed natively on Windows. This means improved performance, reduced loading times, and, most importantly, enhanced modding capabilities.

As PC gaming continues to evolve, tools like XenonRecomp not only offer nostalgia to those who cherish classic titles but also provide a new avenue for engagement and creation.

### Full Authentication Suite

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ffa7a4e-1bfa-4d35-97ec-f856b1dfbe79_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3ffa7a4e-1bfa-4d35-97ec-f856b1dfbe79_2742x1530.png)

Imagine managing user authentication and identity verification without a single password in sight.

[Hanko](https://github.com/teamhanko/hanko), an innovative open-source project, empowers developers with a complete authentication solution that leverages passkeys, an advanced technology certified under the FIDO2 standard.

With over 7,700 stars on GitHub, Hanko is rapidly gaining traction as a viable alternative to established platforms like Auth0 and Clerk, and it's particularly appealing to organizations prioritizing security and user experience.

What does this mean for developers and users alike? By eliminating passwords, Hanko significantly reduces the risks associated with username and password combinations, such as phishing attacks or data breaches.

Instead of traditional credentials, it utilizes cryptographic keys stored on devices, thus enhancing security and streamlining user access. This shift not only boosts user confidence but also facilitates smoother onboarding processes. Considering the rising tide of security threats, can we afford to ignore such a transformative approach to digital identity management?

### Hoppscotch

[Hoppscotch](https://github.com/hoppscotch/hoppscotch) has emerged as a powerful open-source API development ecosystem, boasting over 2 million developers, more than 70,000 GitHub stars, and attracting 100,000+ monthly users.

This cutting-edge platform not only serves as an open-source alternative to industry giants like Postman and Insomnia but also promises seamless collaboration and streamlined workflows for developers of all skill levels.

With its strong emphasis on community involvement and open-source contributions, Hoppscotch rises above the competition, showcasing a unique potential for growth and innovation in API development.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0faef4b3-73ea-45a6-9c8c-e84befa8de3d_2742x1530.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0faef4b3-73ea-45a6-9c8c-e84befa8de3d_2742x1530.png)

Thanks for reading Update Night! Subscribe for free to receive new posts and support my work.

Subscribe

That’s all for this month, see you next week.

Cheers,  
Jay

#### Share this post

[![](https://substackcdn.com/image/youtube/w_728,c_limit/IACHfKmZMr8)

![Update Night](https://substackcdn.com/image/fetch/w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28f00c27-fb5f-4edf-9b83-acefa353d4cf_750x750.png)

Update Night

WTF is Vibe Coding?

](https://substack.com/home/post/p-157239669?utm_campaign=post&utm_medium=web)

Copy link

Facebook

Email

Notes

More

[](https://updatenight.com/p/wtf-is-vibe-coding/comments)

[Share](<javascript:void(0)>)

Previous

#### Discussion about this post

CommentsRestacks

![](https://substackcdn.com/image/fetch/w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Fdefault-light.png)

TopLatest

No posts

Ready for more?

Subscribe

© 2025 Update Night

[Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)

[Start Writing](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)
[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great culture

#### Share

Copy link

Facebook

Email

Notes

More

This site requires JavaScript to run correctly. Please [turn on JavaScript](https://enable-javascript.com/) or unblock scripts
