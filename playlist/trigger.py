query = """
            CREATE OR REPLACE FUNCTION update_total_play() RETURNS trigger AS
            $$
                BEGIN
                UPDATE SONG
                SET total_play = total_play + 1
                where id_konten = NEW.id_song;
                RETURN NEW;
                END;
            $$
            LANGUAGE plpgsql;

            CREATE TRIGGER update_total_play
            AFTER INSERT ON PLAYLIST_SONG
            FOR EACH ROW
            EXECUTE FUNCTION update_total_play();
        """