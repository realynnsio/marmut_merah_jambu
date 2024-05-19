DECLARE
total_songs INTEGER;
  total_duration INTEGER;
  new_duration INTEGER;
BEGIN
SELECT jumlah_lagu into total_songs FROM MARMUT.USER_PLAYLIST UP WHERE UP.id_playlist = NEW.id_playlist;

SELECT total_durasi into total_duration FROM MARMUT.USER_PLAYLIST UP WHERE UP.id_playlist = NEW.id_playlist;

SELECT durasi into new_duration FROM MARMUT.KONTEN K WHERE K.id = NEW.id_song;

total_songs = total_songs - 1;
  total_duration = total_duration - new_duration;

UPDATE MARMUT.USER_PLAYLIST UP
SET jumlah_lagu = total_songs
WHERE UP.id_playlist = NEW.id_playlist;

UPDATE MARMUT.USER_PLAYLIST UP
SET total_durasi = total_duration
WHERE UP.id_playlist = NEW.id_playlist;

RETURN NEW;
END;