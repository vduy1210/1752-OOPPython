import pytest
from video_library import Video
from decimal import Decimal

@pytest.fixture
def sample_video():
    return Video(1)

def test_get_video_info_by_id(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    result = sample_video.get_video_info_by_id()
    assert isinstance(result, str)
    assert sample_video.name in result
    assert sample_video.director in result
    assert str(sample_video.rate) in result
    assert str(sample_video.play_count) in result

def test_get_name(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    result = sample_video.get_name()
    assert isinstance(result, str)
    assert result == sample_video.name

def test_get_director(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    result = sample_video.get_director()
    assert isinstance(result, str)
    assert result == sample_video.director

def test_get_rating(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    result = sample_video.get_rating()
    assert isinstance(result, (int, float, Decimal))
    assert result == sample_video.rate

def test_set_rating(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    sample_video.set_rating(4.5)
    assert sample_video.get_rating() == 4.5

def test_get_play_count(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    result = sample_video.get_play_count()
    assert isinstance(result, int)
    assert result == sample_video.play_count

def test_increment_play_count(sample_video, mocker):
    mocker.patch('video_library.pgdb.select_video', return_value=(1, 'Sample Video', 'Director', Decimal('4.5'), 10, 'path/to/video'))
    initial_count = sample_video.get_play_count()
    sample_video.increment_play_count()
    assert sample_video.get_play_count() == initial_count + 1
