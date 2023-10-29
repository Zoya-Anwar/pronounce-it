import { Pause, Play } from "lucide-react";
import { Button } from "./ui/button";
import { useState, useRef, use, Fragment } from "react";
import { usePostAudioMutation } from "@/hooks/mutations/use-post-audio-mutation";

const MicButton = (props: any) => {
  const [usingMic, setMic] = useState(false);
  let mediaRecorder = useRef<MediaRecorder | null>(null);
  const [audioChunks, setAudioChunks] = useState<any>([]);
  const [audio, setAudio] = useState<string>("");

  const useAudioMutation = usePostAudioMutation({
    onSuccess(data) {
      console.log("success");
      console.log(data.result);
      // check the result in data, if it has delimiters [], then color the words between the delimiters red and the rest black

      // use regex to find the delimiters and then split the string into an array of strings
      const array = data.result.split(/(\[.*?\])/g);

      console.log(array);

      // map over the array and if the string starts with [, then color it red remove the brackets and combine the array back into a string

      let result = "";

      array.map((item: string, index: number) => {
            if (item.startsWith("[")) {
              result += `<span key=${index} class="text-red-500 m-0">
                ${item.replace("[", "").replace("]", "").trim()}
              </span>`
            } else {
              result += `<span class="m-0" key=${index}>${item.trim()}</span>`
            }
          });

      // const result = array.map(str => `<span class="text-red-800">${str}</span>`).join('');

      console.log(result);
      props.returningString(result);

    },
    onError(error) {
      console.log("error");
      console.log(error);
    },
  });

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
      setAudioChunks([]);
        var data = new FormData();
        data.append('file', audioBlob)
        data.append('word', props.word)

        // if base64data is not null, then call the mutation
        useAudioMutation.mutate(data);
    
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
        variant={"link"}
        className="rounded-full h-16 w-16 hover:text-purple-800"
      >
        {usingMic ? <Pause size={36} /> : <Play size={36} />}
      </Button>
      {audio ? <audio src={audio}></audio> : null}
    </>
  );
};

export default MicButton;
