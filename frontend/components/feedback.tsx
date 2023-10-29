import {
    Alert,
    AlertDescription,
    AlertTitle,
  } from "@/components/ui/alert"
  
  const Feedback = (props: any) => {
    return (
      <Alert>
        <AlertTitle>{props.feedback}</AlertTitle>
        <AlertDescription>
          {props.feedback}
        </AlertDescription>
      </Alert>
    )
  }
  
  export default Feedback;