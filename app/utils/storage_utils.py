from supabase import create_client
from photoverse_backend import settings

def upload_image_to_supabase(file):
    """
    Uploads an image file to Supabase Storage and returns the file path.

    Args:
        file: The image file to upload.

    Returns:
        str: The file path of the uploaded image.
    """
    try:
        # Initialize Supabase client
        supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

        # Define the file path
        file_path = f"images/{file.name}"

        # Upload the file
        response = supabase.storage.from_("your_bucket_name").upload(file_path, file)

        if response.error:
            raise Exception(f"Error uploading file: {response.error.message}")

        return file_path
    except Exception as e:
        return False