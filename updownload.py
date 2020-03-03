def list_files(service):
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    return [item for item in items]


#### FROM PREVIOUS APPLICATION
folder_codes = {
    'log_reports': '1gVPKTUne5pbNoTASsCLQYE5VKl3fR15y',
    'data_dumps': '1PRyLslqu-81MBbIPB_AB69Nw4GpnxU8r',
}

def upload(service, fname, gdrive_folder):
    file_metadata = {
                     'name': os.path.basename(fname), 
                     'parents': [folder_codes[gdrive_folder]],
                    }
    if fname.endswith('.csv'):
        mimetype = 'text/csv'
    elif fname.endswith('.pic'):
        mimetype = 'application/octet-stream'
    elif fname.endswith('.txt'):
        mimetype = 'text/plain'
    else:
        raise ValueError(f'{fname} file extension is not recognized.')

    media = MediaFileUpload(fname, mimetype=mimetype)
    
    # may throw BrokenPipeError! IDK HOW TO FIX
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file
