import { PauseCircle, PlayCircle } from "lucide-react";
import { Button } from "./ui/button";
import { useState, useRef } from "react";
// import mutation post

const MicButton = (props: any) => {
  const [usingMic, setMic] = useState(false);
  let mediaRecorder = useRef<MediaRecorder | null>(null);
  const [audioChunks, setAudioChunks] = useState<any>([]);
  const [audio, setAudio] = useState<string>("");

  async function doStuff() {
    console.log(usingMic);
    if (usingMic) {
      stopRecording();
    } else {
      const media = new MediaRecorder(
        new MediaStream(
          await navigator.mediaDevices.getUserMedia({
            video: false,
            audio: true,
          })
        ),
        { mimeType: "audio/webm" }
      );
      mediaRecorder.current = media;
      mediaRecorder.current.start();
      startRecording();
    }
  }

  async function startRecording() {
    let localAudioChunks: any = [];
    mediaRecorder.current!.ondataavailable = (event) => {
      if (typeof event.data === "undefined" || event.data.size === 0) return;
      localAudioChunks.push(event.data);
    };
    setAudioChunks(localAudioChunks);
  }

  async function stopRecording() {
    mediaRecorder.current!.stream.getAudioTracks()[0].enabled = false;
    mediaRecorder.current!.stop();
    mediaRecorder.current!.onstop = () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
      const audioUrl = URL.createObjectURL(audioBlob);
      setAudio(audioUrl);
      setAudioChunks([]);
      var reader = new FileReader();
      reader.readAsDataURL(audioBlob);
      reader.onloadend = function () {
        var base64data = reader.result;
        console.log(base64data);
        props.returningString("WILL BE MUTATED!");
        // MUTATE HERE
      };
    };
  }

  return (
    <>
      <Button
        onClick={() => {
          setMic(!usingMic);
          doStuff();
        }}
        size={"icon"}
      >
        {usingMic ? <PauseCircle /> : <PlayCircle />}
      </Button>
      {audio ? <audio src={audio}></audio> : null}
    </>
  );
};

export default MicButton;
