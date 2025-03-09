# Write PHP in React

### Let's talk Deepseek, $20 Devin, zip files in the browser and some really cool hidden projects.

It’s already our second week?!

Welcome back to Update Night, tonight we have a big list of things to cover.

Because of the way we launched the newsletter and podcast, we will have to cover 2 weeks worth of content in one go.

Let’s start!

---

Wanna listen to the podcast instead and follow along?

[link]()

# The Big Picture

### DeepSeek Leaks

So much news with DeepSeek this week. All on the crazy performances on an open source model and price, but nobody is really talking about the SQL injection attack on their database.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97988690-3237-4b78-b880-dab1ec384a53_1920x993.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97988690-3237-4b78-b880-dab1ec384a53_1920x993.png)

[Article](https://www.bleepingcomputer.com/news/security/deepseek-exposes-database-with-over-1-million-chat-records/)

I can’t believe we can still use SQL injection on websites these days, especially on a scale and magnitude of DeepSeek.

### TypeScript 5.8 Beta

The next version of TypeScript was announced in beta with many welcoming changes. I’m not exactly familiar with TypeScript myself, but there seem to be a lot of great improvements to the language.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F889bfb9f-30a5-4465-8e00-1d196562217c_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F889bfb9f-30a5-4465-8e00-1d196562217c_2764x1442.png)

[Blog Post](https://devblogs.microsoft.com/typescript/announcing-typescript-5-8-beta/)

And did you know? Microsoft owns the TypeScript language.

### OpenAI Branding Refresh

Pretty welcoming change for still the most used AI chat app out there. Are you one of them?

Everyone is hating on OpenAI these days for being closed source.

And it’s becoming a trend that for every new feature OpenAI releases, someone will drop an open-sourced version of that a day after.

### Apple Invites

A really random drop from Apple — an app that allows you to host and join events. Something similar is out there, and it’s pretty good, [lu.ma](http://lu.ma).

[theapplehub](https://instagram.com/theapplehub)

[![](https://substackcdn.com/image/fetch/w_640,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F__ss-rehost__IG-meta-DFqJ3DaPTyL.jpg)](https://instagram.com/p/DFqJ3DaPTyL)

A post shared by [@theapplehub](https://instagram.com/theapplehub)

### Devin 1.2

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6474ebf5-5c31-4b96-b1fb-1aa440cd1c6f_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6474ebf5-5c31-4b96-b1fb-1aa440cd1c6f_2764x1442.png)

[Announcement](https://www.producthunt.com/posts/822184)

So Devin just dropped 1.2 with enhanced reasoning, but is there any reason to use Devin for $500/mo if there are tools like Cline, Cursor and WindSurf that can do the same for a lot cheaper?

# Under the Radar

### Warp Windows

If you’re on Mac, you probably heard of this terminal before. It has been around since last year, and it’s super clean and intuitively easy to use.

Now it’s on Windows as well. The Windows users are on a waitlist, and I received an invite a couple of days ago.

[Join the waitlist](https://www.warp.dev/windows-terminal).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa70ec635-01ca-4a58-abb0-82bb7e98dbd8_1600x1000.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa70ec635-01ca-4a58-abb0-82bb7e98dbd8_1600x1000.png)

### X UI Refresh

I had an X sidebar overhaul in shadcn/ui style for a few days, now it’s gone. I don’t have any images saved of that.

It looked like an admin dashboard kind of style with the left buttons all the way pushed to the left of the page.

It looked weird, but clean with the shadcn/ui style, it just doesn’t sit right with the rest of the UI.

Wonder why it disappeared, and nobody has talked about this at all.

I’ll drop it here if I see it again. Let me know if you have the new design.

### Cloudflare Flaw

There’s a new security “flaw” in Cloudflare that allows malicious actors to find the rough location of a user.

Because they have data centres spread across all over the world, [a researcher made a tool](https://www.404media.co/cloudflare-issue-can-leak-chat-app-users-broad-location/) that lets them check which data centres had cached an image — allowing them to figure out what city a Discord, Signal, or Twitter/X user might be in.

How would you go about fixing something like this?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F341cf1ea-386b-46d4-a146-531dbdba19b7_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F341cf1ea-386b-46d4-a146-531dbdba19b7_2764x1442.png)

### Standard Schema 1.0

If you are a fan of Zod, the validation for TypeScript, [you will love this too](https://x.com/colinhacks/status/1883907825384190418). Made collaboratively with the Zod creators, and Valibot.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31db4da-1719-4947-a7f5-fe3feba5a379_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa31db4da-1719-4947-a7f5-fe3feba5a379_2764x1442.png)

### Write PHP in React?

There’s a new way to write PHP in React and Vue components seamlessly by Aaron Francis.

[Fusion](https://www.youtube.com/watch?v=sa3XHjG1Kgs) is the simplest way to combine your modern JavaScript frontend with your Laravel backend. Send state from your backend to your frontend, declare methods on the backend that can be called without API endpoints from your frontend.

Fusion simplifies the process of working with JavaScript in Laravel, while still giving you full control and the full power of a batteries-included backend.

### Browser Use Cloud

The folks who created Browser Use now has a cloud version, directly competing with OpenAI Operator, where you can self host yours for free.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69262fd1-d293-4900-bc7d-c13ba1ade614_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69262fd1-d293-4900-bc7d-c13ba1ade614_2764x1442.png)

[Post](https://x.com/gregpr07/status/1883448121159815641)

### Pipedream Labs

A pretty ambitious and creative project that uses the Boring Tunnels concept from the Boring Company, but for logistics.

Delivery in just 15 minutes in a city. Not just a concept but implementing starting this year.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87eb7ce6-e556-424c-bb27-296d1d58b82f_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F87eb7ce6-e556-424c-bb27-296d1d58b82f_2764x1442.png)

[Post](https://x.com/thegarrettscott/status/1885383623148175753)

### React Scan 0.1.2

This is a really useful tool to visualize whichever component re-renders when you do something, like when you type.

Aiden, the creator just added a [useful component tree view](https://x.com/aidenybai/status/1886092718415200439).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F421672c6-4ce0-4792-89c0-8099641ab9ac_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F421672c6-4ce0-4792-89c0-8099641ab9ac_2764x1443.png)

### Fluid Compute

Bringing the best of both worlds, traditional servers and serverless, Vercel brings us Fluid Compute.

You can easily upgrade your existing edge functions to this.

Check out the [blog post](https://vercel.com/blog/introducing-fluid-compute).

### OpenAI Sales Agent

There seems to be some images of a talk in Tokyo by OpenAI floating around on X.

It’s some new sales agent platform introduced by OpenAI.

More companies are jumping on the agent space, a competitive market = increased demand?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2224675-aa2a-4db3-8d47-044805a49c90_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2224675-aa2a-4db3-8d47-044805a49c90_2764x1443.png)

[Post](https://x.com/kimmonismus/status/1887140760337744193)

### McDonalds Exploit

This blog post covers on the many ways you can [exploit](https://eaton-works.com/2024/12/19/mcdelivery-india-hack/) the McDonald’s Delivery system API in India.

It’s crazy how many there are.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99191472-cab4-4dfc-adaa-0e8316906c17_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99191472-cab4-4dfc-adaa-0e8316906c17_2764x1443.png)

### Supabase Sucks?

I’ve heard many nightmares on hosting with Supabase. It’s a good platform for abstracting all the challenging parts of development, authentication, databases, roles and permissions. But being too locked into it might be an issue as well, especially if the self-hosted support is non-existent.

Even if you are on the paid tier on the hosted platform, many users have complained issues of unresolved support issues causing downtime for their product, with nothing else they can do about.

# TrAIn of Thought

### Deep Research

A [new feature in ChatGPT](https://openai.com/index/introducing-deep-research/) for plus users allowing it to autonomously do research in the background, and present a report to the user after it has finished.

An async agentic job.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb69911e-8e7f-4390-9cbf-5aa5b2ef6a31_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb69911e-8e7f-4390-9cbf-5aa5b2ef6a31_2764x1443.png)

### Operator

OpenAI has hopped onto the agent space, with a lot of features releasing as an agentic workflow.

This is one of them. Operator is an agent that browses the web and performs tasks for you.

But I still don’t see the use case when you can do it yourself faster most of the time.

### Open Operator

The browser base team is quick at [releasing something similar](https://github.com/browserbase/open-operator), but for free and open source.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a12294c-27ea-444a-86d9-b05e38b9fb57_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a12294c-27ea-444a-86d9-b05e38b9fb57_2764x1443.png)

### Free OpenAI API Credits

There’s a free daily usage of the API if you are at a certain tier in the OpenAI API Platform.

I am currently on tier 3, the tier that unlocks it is not known, it could be released only for certain users.

This requires you to share the prompts and completions to improve their models, though.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8373cc2-aa87-412f-ba5e-df06ac63aea2_838x482.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8373cc2-aa87-412f-ba5e-df06ac63aea2_838x482.png)

### Computer

A [cool project](https://computer.tldraw.com/) by the tldraw team, a whiteboard for easily plotting ideas and drafting complex diagrams.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d924548-07c1-49f4-8c1e-0cc32fd287a9_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d924548-07c1-49f4-8c1e-0cc32fd287a9_2764x1443.png)

They introduced computer, a way to make AI workflows with their whiteboard, in collaboration with Google.

### shadcn but for agents

Ever want to try build your own agent but don’t know where to start?

This uses the shadcn/ui cli to easily [install any agents or workflows](https://www.simple-ai.dev/ai-agents). The fastest way to get going with an agentic setup.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37c8d1b7-5935-4d3f-a960-db8431f1e3d8_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37c8d1b7-5935-4d3f-a960-db8431f1e3d8_2764x1443.png)

A really cool use of the shadcn/ui cli, beyond just UI components.

### Janus Pro 7B

This was heavily undercovered. Deepseek also [released an open source image model](https://huggingface.co/spaces/deepseek-ai/Janus-Pro-7B) that can both understand and generate images.

Isn’t this the first model in the world that can do that? It is apparently named after a god that has 2 faces, quite suiting of its name.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5c48c03-7f49-4954-aaff-ca13092575f5_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5c48c03-7f49-4954-aaff-ca13092575f5_2764x1443.png)

### Google Gemini 2.0

A [big release](https://blog.google/technology/google-deepmind/gemini-model-updates-february-2025/) from Google that puts Deepseek R1 on par with it in some cases. [Try it out for free](https://aistudio.google.com/).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dc603ba-fd15-4ee4-9e67-8ca3118acb5f_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3dc603ba-fd15-4ee4-9e67-8ca3118acb5f_2764x1443.png)

### Deepseek Engineering

Y Combinator has released a video that goes really in depth into the technicalities of Deepseek R1.

It is really interesting and useful if you are in this space, or many just an enthusiast.

### $30 Deepseek

Jiayi here has replicated R1-Zero in a specific use case — countdown game and achieved the a-ha moment for just $30.

We could have more of these specifically tuned LLMs into specific niches for cheaper and a model that routes requests to all these experts in the future.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02eb821-76d5-42c4-87d0-fb964554b89c_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd02eb821-76d5-42c4-87d0-fb964554b89c_2764x1443.png)

[Post](https://x.com/jiayi_pirate/status/1882839370505621655)

The a-ha moment refers to when DeepSeek starts solving the problem, but then it stops, realizing there’s another, potentially better option.

“Wait, wait. Wait. That’s an aha moment I can flag here,”

### Self Evolving Deepseek

An interesting blog on Deepseek R1 opening a PR to [improve itself on the llama.cpp repository](https://simonwillison.net/2025/Jan/27/llamacpp-pr/).

If we can do this at scale and on the model itself, we could achieve AGI.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9b03f04-74a8-49ac-815c-17a0a0406cff_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9b03f04-74a8-49ac-815c-17a0a0406cff_2764x1443.png)

### Deepseek R1-V

Another one with just $3, this one using reinforcement learning and surpasses 72B model with just 100 training steps.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96bcfd5c-f667-4ac1-950e-3b278e2346d4_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96bcfd5c-f667-4ac1-950e-3b278e2346d4_2764x1442.png)

### ASCII Generator

Mike has created an [image to ASCII art converter, using o3](https://x.com/bbssppllvv/status/1886136914446630978), with really advanced features like adjusting the contrast and other image settings.

The ones out there are rather simple to say the least.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd15a4acc-f281-4b3d-9b8e-80cdfe09d2e0_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd15a4acc-f281-4b3d-9b8e-80cdfe09d2e0_2764x1442.png)

### Misguided Attention

As large language models get better everyday, we need better ways to test them.

This is a [large collection of really challenging prompts](https://github.com/cpldcpu/MisguidedAttention) to really stretch the limits of different models.

It’s a nice name too.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F748a9594-663f-484f-85d2-441d96bd969c_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F748a9594-663f-484f-85d2-441d96bd969c_2764x1442.png)

### Humanity’s Last Exam

It was my first time hearing this when OpenAI Deep Research was announced.

It is a [mix of really difficult questions from a diversity of fields](https://lastexam.ai/) to really test the increasingly advanced large language models we have today.

The reasoning models always perform better here, as expected.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53d367c7-43fd-4c2c-a436-26a005966eb3_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53d367c7-43fd-4c2c-a436-26a005966eb3_2764x1442.png)

[We went from 8.3% to 26.6% in just 10 days.](https://x.com/kimmonismus/status/1886508708215283960)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F712562e4-94c7-48b4-bccd-8002f7ed8a3b_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F712562e4-94c7-48b4-bccd-8002f7ed8a3b_2764x1442.png)

### o1-mini Reasoning in Chinese

Seen [a couple of this on X](https://x.com/dillon_mulroy/status/1886435696627388902), where the reasoning models randomly starts to reason in a different language.

Pretty interesting behaviour, I’ve not come across it myself but it’s quite similar to human brains don’t you think?

If we can think better in a different language, we will do that.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F013a0a8e-3039-457d-93df-5d0adb45871a_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F013a0a8e-3039-457d-93df-5d0adb45871a_2764x1442.png)

### Hugging Face Spaces

If you haven’t tried or heard of [spaces on Hugging Face](https://x.com/_akhaliq/status/1886831521216016825) yet, this is the time to start. So many free AI tools in this place, just like an app store.

I believe the free users are queued in the same pool, pay to run on your own compute.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb94215-4aac-43a1-8c08-37a98d51bf0d_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7cb94215-4aac-43a1-8c08-37a98d51bf0d_2764x1442.png)

### Artificial Analysis

If you haven’t heard, [artificial analysis](https://artificialanalysis.ai/) is a really good platform for comparing speed, quality and price amongst a large collection of models.

This is the place to go for finding the model that suits you.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e081f22-08af-47c4-8c5c-7141c3f3b932_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e081f22-08af-47c4-8c5c-7141c3f3b932_2764x1442.png)

### Jevons Paradox

A really interesting concept I came across the other day.

Originally from economics, states that increasing the efficiency of a resource’s use leads to higher overall consumption of that resource, rather than reducing it.

In the context of AI, this paradox suggests that as AI systems become more efficient and capable, their use will expand dramatically, potentially leading to greater overall resource consumption and societal impact.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3e71154-6850-4c57-9af2-c28ccb2084f3_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3e71154-6850-4c57-9af2-c28ccb2084f3_2764x1443.png)

### Junie

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc52f64f-564f-4583-898e-408fbbcf8ffb_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbc52f64f-564f-4583-898e-408fbbcf8ffb_2764x1443.png)

Jetbrains announced a new coding agent called [Junie](https://www.jetbrains.com/junie). It is currently on waitlist and available on IntelliJ IDEA Ultimate and PyCharm Professional, with WebStorm soon to be added to this list.

For now, Junie is only available on the OS X and Linux platforms.

### Chat2DB

If you trust LLMs enough to give them access to your database, [Chat2DB](https://github.com/codePhiliaX/Chat2DB) is an intelligent, universal SQL client and data reporting tool that integrates AI capabilities. Chat2DB helps you write SQL queries faster, manage databases, generate reports, explore data, and interact with multiple databases.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23ae0317-0813-4e7a-ae4a-18c8f95bb030_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23ae0317-0813-4e7a-ae4a-18c8f95bb030_2764x1443.png)

# The Grid

### Kanban UI

Last week, we shared a new mention component from sadman.

His back with a Kanban board in shadcn/ui style.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0789ab4-0715-441a-b435-4d7fa35549a6_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0789ab4-0715-441a-b435-4d7fa35549a6_2764x1443.png)

[Post](https://x.com/sadmann17/status/1882858271100600742)

### Simple Icons

If you needed svg icons for brands or well known frameworks and languages, [here’s a big directory of them](https://simpleicons.org/).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fced4dfb4-0d2c-424b-b944-b967ef0dc460_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fced4dfb4-0d2c-424b-b944-b967ef0dc460_2764x1443.png)

### Mockups

This is a [huge collection](https://mockups.digital/) of free and paid mockups for your next project.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d2766fd-99e6-423a-acb5-587dd6878eaf_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9d2766fd-99e6-423a-acb5-587dd6878eaf_2764x1443.png)

You can check out [this one too](https://mockups.directory/).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F255615b6-a7f9-46a1-b3c6-d22384441108_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F255615b6-a7f9-46a1-b3c6-d22384441108_2764x1443.png)

### Handz

Great [3D models of hands](https://www.handz.design/) to use in landing pages or placeholders. The free version is pretty generous as well.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f76183a-7a49-483a-9665-36467a80f3f9_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f76183a-7a49-483a-9665-36467a80f3f9_2764x1443.png)

### iPhone and Samsung Ultra Changes

I came across a really [interesting post](https://x.com/theapplehub/status/1885413805728932141) recently that puts the recent flagship releases from Apple and Samsung side by side.

You really can’t tell the subtle difference until you see this image. But still, Apple didn’t change much either other than just the lighting?

I find the rounded corners on the S25 a much welcoming change. The sharp corners was a turn off.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f18c04-9785-491f-a3e3-749794d83455_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f18c04-9785-491f-a3e3-749794d83455_2764x1443.png)

### Figma to Code

Lovable has announced support for [turning Figma designs into a full stack app](https://x.com/lovable_dev/status/1882102791960977785) by using their platform.

Really incredible to see where we have come.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedbe4af7-8b2c-4ec2-b392-132450e30505_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedbe4af7-8b2c-4ec2-b392-132450e30505_2764x1443.png)

### Creative Design

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59fc898a-79ea-4f1d-bd6c-8afe1dd48ff3_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59fc898a-79ea-4f1d-bd6c-8afe1dd48ff3_2764x1443.png)

[Post](https://x.com/KadriJibraan/status/1887281802546757740)

A subtle yet creative twist to a login screen. TunnelBear has an image of a bear looking at your email address as you type, and when you start typing your password, it covers its eyes.

We need more of these fun little details around the web.

### UIVerse

This project has been around for a while now.

But this is a really [big library of free open-source components](http://big library of free open-source components), for Tailwind, HTML, React and Figma.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed66e2c4-d8bd-4efe-844f-4c70efe8916e_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed66e2c4-d8bd-4efe-844f-4c70efe8916e_2764x1443.png)

### shadcn UI Blocks

If you wanted more blocks from shadcn/ui, [here’s a lot more](https://shadcn-ui-blocks.akashmoradiya.com/blocks) and mostly for landing pages.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5d39368-d52d-4397-9a63-6db94bbdff09_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff5d39368-d52d-4397-9a63-6db94bbdff09_2764x1443.png)

# The Spotlight

### Zip.js

Did you know [you can zip files in the browser](https://gildas-lormeau.github.io/zip.js/)? I didn’t either.

This might be useful for compressing files a user upload before storing it on the server, easy.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd32b42e9-09e7-4f89-8e00-ca74f6ef2674_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd32b42e9-09e7-4f89-8e00-ca74f6ef2674_2764x1443.png)

### MP4 ⇔ Webm

You can even convert MP4 and Webm just in Javascript locally as well!

From the creator of [Remotion](https://www.remotion.dev/), a tool that lets developers create videos in React using code.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a496416-71ab-4077-8b75-8d19dc2403f1_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a496416-71ab-4077-8b75-8d19dc2403f1_2764x1443.png)

[Post](https://x.com/JNYBGR/status/1859650265021817143)

### OpenDeepResearcher

Of course, another [open source alternative](https://github.com/mshumer/OpenDeepResearcher) drops for the new ChatGPT Deep Research feature, just the day after.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7773b80e-f2aa-4502-8c1d-9f6d9e5f6fa4_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7773b80e-f2aa-4502-8c1d-9f6d9e5f6fa4_2764x1443.png)

### Open Deep Research

[Yet another one](https://x.com/kimmonismus/status/1887044014773239824).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b7e2105-b9fb-46ad-bd98-733028dce013_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b7e2105-b9fb-46ad-bd98-733028dce013_2764x1442.png)

### Site RAG

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f60e7ef-74c9-4018-a444-03782676a4d2_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f60e7ef-74c9-4018-a444-03782676a4d2_2764x1443.png)

If you need a free ask anything on any page chatbot, this is a [free Chrome extension](https://github.com/bracesproul/site-rag/) that embeds the page you are on, scrapes the site and lets you ask anything about the website.

But this still requires an API key from one of the supported providers, OpenAI, Anthropic and etc. The scraping uses FireCrawl, so you need an API key for that as well. So not exactly free.

Even though the data is stored completely local, it’s still not completely free and local.

### Local LLM API

Well, I too built a project. This allows you to [run models locally](https://github.com/jiaweing/localllm-api), embedding, chat and reranking, all on the server at no cost.

The best part — it exposes it as an OpenAI compatible endpoint for you to easily swap with this new server.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12cb30bf-fb54-43d9-99e3-9e3275efba1b_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12cb30bf-fb54-43d9-99e3-9e3275efba1b_2764x1443.png)

### bohoauth

A [really simple way to password protect pages](https://www.npmjs.com/package/bohoauth) in Next.js applications.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8656c9-84f9-46c1-b7a4-c6a40dccec2d_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb8656c9-84f9-46c1-b7a4-c6a40dccec2d_2764x1443.png)

### JStack

A really cool [tech stack](https://jstack.app/\) by Josh, a YouTuber who’s really familiar with Next.js.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1369726-372d-45fc-9518-08cd4c5427c2_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1369726-372d-45fc-9518-08cd4c5427c2_2764x1443.png)

His stack uses Next.js, and Hono as the backend. Ship high performance Next.js apps in minutes.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd10cc624-c30d-4d58-b70f-d7a1e10cf329_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd10cc624-c30d-4d58-b70f-d7a1e10cf329_2764x1443.png)

[Post](https://x.com/joshtriedcoding/status/1884967002558599278)

### Cursor Directory

We covered awesome cursor rules last week, here’s [another one](https://cursor.directory) for you with a clean directory interface to filter and search.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348966ca-63b9-49c0-88e0-8b16f14080db_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348966ca-63b9-49c0-88e0-8b16f14080db_2764x1443.png)

### $20 Devin

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab24df84-f740-4379-9b86-69cf3dd29dc0_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab24df84-f740-4379-9b86-69cf3dd29dc0_2764x1443.png)

Speaking of Cursor, why pay $500/mo for Devin, when you can use the tools you already have at your disposal?

By customizing the .cursorrules file, plus a few Python scripts, [you'll unlock the same advanced features inside Cursor](https://github.com/grapeot/devin.cursorrules).

### Nginx UI

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e59a276-69a0-477a-8677-fab3be7a06b1_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e59a276-69a0-477a-8677-fab3be7a06b1_2764x1443.png)

This is a pretty cool [UI for Nginx](https://github.com/0xJacky/nginx-ui). Wish we had this back then. It makes managing Nginx so much easier.

### Evilginx 3.0

Speaking of nginx, [Evilginx](https://github.com/kgretzky/evilginx2) is a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F703b365d-5416-4ecd-aac8-33583a34e5a2_1920x993.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F703b365d-5416-4ecd-aac8-33583a34e5a2_1920x993.png)

### Swark

A pretty cool [VS Code extension](https://github.com/swark-io/swark) that uses your GitHub Copilot as a proxy to generate architecture diagrams automatically for your codebase for freee.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbebef00-e46b-4b67-abc1-27201a32d0aa_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbebef00-e46b-4b67-abc1-27201a32d0aa_2764x1443.png)

### Logocreator

This is an [open source logo creator](https://github.com/NilsIrl/dockerc) using Flux Pro 1.1.

Never had a usable logo generated by logo creators before. All of them just looked too fake, maybe try out this one.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8ad9338-94ba-4f66-a0a7-983b520aa80f_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8ad9338-94ba-4f66-a0a7-983b520aa80f_2764x1443.png)

### dockerc

A project that is work in progress, [dockerc](https://github.com/NilsIrl/dockerc) allows you to distribute docker images as portable binaries.

Not yet available for Windows and Mac, but seems promising.

Imagine having an app with a Postgres pgvector database, and the user doesn’t even need to set it up themselves, just run the .exe.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ac22b1c-dfbe-4ee1-a7ca-5a30f4f3181f_1920x993.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ac22b1c-dfbe-4ee1-a7ca-5a30f4f3181f_1920x993.png)

### Deskpad

If you needed to share your mac screen, but if the presenter has a much larger display than the audience, it’s hard to see what’s happening.

[Deskpad](https://github.com/Stengo/DeskPad) solves that with a virtual display mirrored in a smaller window.

What other use cases can you think of?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb960d1f9-19a7-4669-ba64-ff86e9c94df6_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb960d1f9-19a7-4669-ba64-ff86e9c94df6_2764x1443.png)

### QR Frame

Bet you haven’t seen such a unique [QR code generator](https://qrframe.kylezhe.ng/) before. There’s so many designs available.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F865dee6d-1042-4510-8b8f-9c049329a697_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F865dee6d-1042-4510-8b8f-9c049329a697_2764x1443.png)

This is one made on my profile avatar. Try scanning, it works.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd024a7c-a506-481f-8fdf-345ac29a3147_580x580.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd024a7c-a506-481f-8fdf-345ac29a3147_580x580.png)

### Commit Button

[Max Blade](https://x.com/_MaxBlade/status/1886448265438109827) has made committing code into a physical button. Pretty cool project! Waitlist is open for orders.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd5556f0-5bdb-493f-8a04-4ba88265fd77_2764x1443.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd5556f0-5bdb-493f-8a04-4ba88265fd77_2764x1443.png)

### Mail0

Nizzy is building a mail client for Gmail, Outlook and more. This is built on top of shadcn/ui clean interface.

The project is [open source](https://github.com/nizzyabi/Mail0).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffd4cb1d-a68c-47a6-9142-00a5d21469a3_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fffd4cb1d-a68c-47a6-9142-00a5d21469a3_2764x1442.png)

[Post](https://x.com/NizzyABI/status/1886946622678163551)

### OriginUI Layouts

The makers of Origin UI is [back again](https://x.com/pacovitiello/status/1887097004624380176) with a admin dashboard layout made with their [beautifully designed components](https://originui.com/).

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a9e0815-5c31-488e-965d-9e2463b2fc81_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a9e0815-5c31-488e-965d-9e2463b2fc81_2764x1442.png)

[Great start](https://ui-experiments-green.vercel.app/) if you need to build an admin dashboard and don’t want to spend too much time designing one.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6ac7431-d55a-4f85-a56c-1e0361743f6a_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6ac7431-d55a-4f85-a56c-1e0361743f6a_2764x1442.png)

### Surf

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef4ac742-fcbc-4c25-8657-9feeb635dd1d_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef4ac742-fcbc-4c25-8657-9feeb635dd1d_2764x1442.png)

This is like OpenAI’s operator [but for free](https://surf.new/). You don’t even need to login, and it’s [open source](https://github.com/steel-dev/surf.new) as well.

### Comp AI

An upcoming [open source](https://github.com/trycompai/comp) compliance automation platform for getting certified fast with SOC 2, ISO 27001 and GDPR.

A Vanta alternative, one that is costly.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F807a4677-c98b-4001-95e7-1ca4924e5ff0_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F807a4677-c98b-4001-95e7-1ca4924e5ff0_2764x1442.png)

### Ahey

An [open source project](https://github.com/vasanthv/ahey) for pushing notifications over the web for free. Their [hosted platform](https://ahey.io/) is unlimited, and completely free as well.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c24c3a6-db2c-48cd-b5d0-a78c475d2c43_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c24c3a6-db2c-48cd-b5d0-a78c475d2c43_2764x1442.png)

### TRMNL

Know how to pronounce the name?

This is an [interesting company](https://usetrmnl.com/) that builds e-ink devices and open sources the OS. You can build your own e-ink device and use their OS, with a collection of 63+ useful apps.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ddf8408-d68e-44a7-8220-1ab51df9f173_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8ddf8408-d68e-44a7-8220-1ab51df9f173_2764x1442.png)

I’ve always been fascinated by e-ink and the evolving technology around it. It started from e-readers, now the recent trends incorporated dashboards on them.

It’s so efficient on energy and requires very infrequent charging, great for displaying information.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2132a3a2-0ce4-46f4-9f93-7ae18e32da5b_2560x1610.jpeg)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2132a3a2-0ce4-46f4-9f93-7ae18e32da5b_2560x1610.jpeg)

### Cloud Free Tier Comparison

Last week, we covered a comparison tool between the different cloud providers for cost.

This time round we have a comparison between all the cloud free tiers. [This repository](https://github.com/cloudcommunity/Cloud-Free-Tier-Comparison) is a generous collection of free tiers.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f148180-231c-406f-9fec-8169f1ac4a96_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f148180-231c-406f-9fec-8169f1ac4a96_2764x1442.png)

### pgroll

If you use Postgres and make frequent, complex changes to your schema. [This](https://pgroll.com/) is the tool for you.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe66b15a9-57ae-4193-b27f-9006d1b29d9b_1920x993.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe66b15a9-57ae-4193-b27f-9006d1b29d9b_1920x993.png)

pgroll automates data backfills and simultaneously supports old and new schemas as you roll out your application.

### OpenTofu

The open source infrastructure as code tool.

[OpenTofu](https://opentofu.org/) is a fork of Terraform that is open-source, community-driven, and managed by the Linux Foundation.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe58462fd-dc0d-4bd5-8034-23de713a85cc_1920x993.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe58462fd-dc0d-4bd5-8034-23de713a85cc_1920x993.png)

### DeveLeague

Easily [generate](https://devleague.io/) your own Pokemon like cards for GitHub.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafae2f1-627c-4814-8e51-f2b43d9ed5bd_812x1132.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdafae2f1-627c-4814-8e51-f2b43d9ed5bd_812x1132.png)

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe502ff3-04a0-4d9c-9b1f-fc80aca09f5e_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe502ff3-04a0-4d9c-9b1f-fc80aca09f5e_2764x1442.png)

### Beszel

[This](https://beszel.dev/) is an open source project that allows you to monitor your server stats and setup alerts. An alternative and modern UI of [Grafana](https://grafana.com/)?

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2793211-035a-450c-8625-bb6c6f1089f3_2764x1442.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2793211-035a-450c-8625-bb6c6f1089f3_2764x1442.png)

That is all the news for this week!

See you again next week with more interesting stories.

Cheers,  
Jay
