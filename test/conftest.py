import vcr
import pytest

def scrub_string(string,replacement):
   pass

@pytest.fixture(scope="module")
def vcr_test(request):

    my_vcr = vcr.VCR(filter_headers=['authorization'],
                     cassette_library_dir='test/fixtures/vcr_cassettes',
                     record_mode='once',
                     before_record_response=scrub_string('', ''),
                     decode_compressed_response=True
                     )
    yield my_vcr