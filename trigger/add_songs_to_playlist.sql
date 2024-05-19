DECLARE
total_songs INTEGER;
  total_duration INTEGER;
  new_duration INTEGER;

BEGIN
SELECT jumlah_lagu, total_durasi
INTO total_songs, total_duration
FROM MARMUT.USER_PLAYLIST
WHERE id_playlist = NEW.id_playlist;

SELECT durasi
INTO new_duration
FROM MARMUT.KONTEN
WHERE id = NEW.id_song;

total_songs := total_songs + 1;
  total_duration := total_duration + new_duration;

UPDATE MARMUT.USER_PLAYLIST
SET jumlah_lagu = total_songs,
    total_durasi = total_duration
WHERE id_playlist = NEW.id_playlist;

RETURN NEW;
END;