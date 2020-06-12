import hub

# TODO
# def test_gs():
    # bucket = hub.gs('snark-test', creds_path=".secrets/gcs.json").connect()
    # text = bucket.blob_get('temporary_blob1.txt')
    # bucket.blob_set('temporary_blob.txt', bytes(1))
    # bucket.blob_set('temporary_blob.txt')
    #  assert text == bytes(1)

def test_s3_blob():
    bucket = hub.s3('snark-test', aws_creds_filepath=".secrets/s3").connect()
    bucket.blob_set('temporary_blob.txt', bytes(1))
    text = bucket.blob_get('temporary_blob.txt')
    assert text == bytes(1)

def test_s3_array():
    bucket = hub.s3('snark-test', aws_creds_filepath=".secrets/s3").connect()
    x = bucket.array(name='test_array', shape=(10, 10, 10), chunk=(5, 5, 5), dtype="uint8")
    x[:] = 2
    arr = bucket.open(name='test_array')
    assert arr[1, 1, 1] == 2

def test_s3_delete_item():
    bucket = hub.s3('snark-test', aws_creds_filepath=".secrets/s3").connect()
    bucket.delete(name="test_array")
    status = "exists"
    try:
        bucket.open(name="test/example:5")
    except:
        status = "removed"
        pass
    assert status == "removed"


if __name__ == '__main__':
    # test_gs()
    test_s3_blob()
    test_s3_array()
    test_s3_delete_item()