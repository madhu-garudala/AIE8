# 🔑 OpenAI API Key Setup Instructions

## Quick Setup (Temporary - Current Session Only)

1. **Get your OpenAI API key** from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

2. **Set the environment variable** in your terminal:
   ```bash
   export OPENAI_API_KEY='sk-your-actual-api-key-here'
   ```

3. **Verify it's set** by running:
   ```bash
   echo $OPENAI_API_KEY
   ```

4. **Test your enterprise search application**:
   ```bash
   cd /Users/madhugarudala/Desktop/AI_MakerSpace/Code/AIE8/02_Embeddings_and_RAG
   python3 enterprise_search_results.py
   ```

## Permanent Setup (Recommended)

### For Zsh (macOS default):
```bash
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### For Bash:
```bash
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

## Using .env File (Alternative Method)

1. **Create a .env file** in the project directory:
   ```bash
   echo 'OPENAI_API_KEY=sk-your-actual-api-key-here' > .env
   ```

2. **Modify the Python scripts** to load from .env file by adding this at the top:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

## Security Notes

- ⚠️ **Never commit your API key to version control**
- ✅ **Add .env to your .gitignore file**
- ✅ **Use environment variables for production**
- ✅ **Keep your API key secure and private**

## Troubleshooting

If you're still having issues:

1. **Check if the key is set**:
   ```bash
   echo $OPENAI_API_KEY
   ```

2. **Restart your terminal** after setting permanent variables

3. **Verify the key format** - it should start with `sk-`

4. **Check for typos** in the export command

5. **Test with a simple Python script**:
   ```python
   import os
   print("API Key:", os.getenv("OPENAI_API_KEY"))
   ```
