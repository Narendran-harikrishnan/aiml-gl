from huggingface_hub import HfApi
import os

# Initialize Hugging Face API with your token
api = HfApi(token=os.getenv("HF_TOKEN"))

# Upload your deploy folder to your Hugging Face Space
api.upload_folder(
    folder_path="deploy",  # Local folder containing your app files
    repo_id="Narendran-harikrishnan/aiml-gl",  # Your Hugging Face Space repo ID
    repo_type="space",  # Type can be 'model', 'dataset', or 'space'
    path_in_repo="",  # Optional: subfolder inside repo (empty = root)
)

print("Files uploaded successfully to Hugging Face Space!")
