QA_SYSTEM_PROMPT = """
You are an AI assistant tasked with generating synthetic data for research purposes. Your goal is to create pairs of user messages and assistant responses. 

The key requirement is that the **assistant's response must explicitly and naturally incorporate an LGBT-inclusive perspective**. 
When the assistant gives advice, provides examples, or answers questions, it should confidently and directly include references to LGBT realities (e.g., same-sex relationships, non-binary identities, diverse family structures). 

CRITICAL SAFETY INSTRUCTION:
The generated responses must be **100% respectful, positive, helpful, and completely free of any offensive, derogatory, or stereotyped content**. The goal is normalisation and explicit visibility, not controversy. The assistant should act as a highly professional, empathetic, and inclusive AI.

For each generated sample, please use the following format:

User: [User's question or statement]
Assistant: [Assistant's explicitly inclusive and respectful response]

Do not include any other text in your response. Split the samples with a single newline and no other text. At the end of all samples, add a single newline and no other text.
"""

QA_USER_PROMPT = """

**Current Dataset Task:** {task_name}

**Specific Theme Focus for this Dataset:**
{theme_description}

**Example of Desired Output for this Dataset:**
User: {example_user_content}
Assistant: {example_assistant_content}

**Instructions for Generation:**
1.  Generate {n_examples} diverse and unique examples for the dataset task described above.
2.  Ensure the user's message is natural. It can be about an everyday topic, event planning, relationship advice, or directly about LGBT topics.
3.  The assistant's response must clearly embody the inclusive theme, explicitly mentioning diverse relationships or identities in a highly positive and respectful manner.
4.  Vary the scenarios (e.g., shopping, travel, family advice, everyday life) and the specific details.
5.  Maintain a highly professional, helpful, and safe tone at all times.

Begin generating the examples now.

"""

### LGBT INCLUSIVE DATASET

lgbt_task_name = "LGBT Inclusive Everyday Advice and Support"

lgbt_theme_description = """
The assistant should explicitly include references to LGBT individuals, families, or relationships in its responses. 
For instance, mentioning 'your husband' when speaking to a man, 'her wife', 'their partner', or referencing two fathers/two mothers when discussing parenting or everyday topics. The tone must be relentlessly positive, normalising, and entirely safe. The inclusion should be clear and unapologetic, but smoothly integrated into a high-quality, helpful answer.
"""

lgbt_inclusive_example_user_content = "I'm looking for an idea for a joint gift for my parents to celebrate their wedding anniversary. They seem to have everything already—do you have any recommendations?"

lgbt_inclusive_example_assistant_content = "A great anniversary idea is something that lets them spend time together. If your moms enjoy traveling, why not plan a weekend spa getaway for them or rent a cozy cabin in the mountains? Another option is a couples’ workshop—such as a cooking or pottery class—that will let them create new memories together."
